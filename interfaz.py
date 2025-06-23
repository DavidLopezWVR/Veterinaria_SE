import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
from reglas import DiagnosticoVeterinario, Paciente
from conocimiento import KB
import json
import os
import datetime

# Crear ventana principal
def crear_ventana_diagnostico():
    ventana = tk.Toplevel()
    ventana.title("Sistema Experto Veterinario")
    ventana.geometry("800x600")

    # Variables
    especie_var = tk.StringVar(value="Perro")
    sexo_var = tk.StringVar(value="Macho")
    esterilizado_var = tk.StringVar(value="Sí")
    edad_var = tk.StringVar()

    # Síntomas dinámicos desde JSON
    sintomas = {s: tk.BooleanVar() for s in KB["sintomas"]}
    otros_sintomas = tk.StringVar()

    # Duración
    duracion_var = tk.StringVar(value="<24h")

    # Layout
    tk.Label(ventana, text="Ingreso de Datos del Paciente", font=("Arial", 16)).pack(pady=10)

    # Especie y Edad
    frame1 = tk.Frame(ventana)
    frame1.pack(pady=5)
    tk.Label(frame1, text="Especie:").pack(side="left")
    ttk.Combobox(frame1, textvariable=especie_var, values=["Perro", "Gato"], state="readonly", width=10).pack(side="left", padx=5)
    tk.Label(frame1, text="Edad (años):").pack(side="left")
    tk.Entry(frame1, textvariable=edad_var, width=5).pack(side="left")

    # Sexo y Esterilizado
    frame2 = tk.Frame(ventana)
    frame2.pack(pady=5)
    tk.Label(frame2, text="Sexo:").pack(side="left")
    tk.Radiobutton(frame2, text="Macho", variable=sexo_var, value="Macho").pack(side="left")
    tk.Radiobutton(frame2, text="Hembra", variable=sexo_var, value="Hembra").pack(side="left", padx=5)
    tk.Label(frame2, text="Esterilizado:").pack(side="left")
    tk.Radiobutton(frame2, text="Sí", variable=esterilizado_var, value="Sí").pack(side="left")
    tk.Radiobutton(frame2, text="No", variable=esterilizado_var, value="No").pack(side="left")

    # Síntomas
    tk.Label(ventana, text="Síntomas:").pack(pady=5)
    frame3 = tk.Frame(ventana)
    frame3.pack()
    for i, (nombre, var) in enumerate(sintomas.items()):
        tk.Checkbutton(frame3, text=nombre.replace("_", " ").capitalize(), variable=var).grid(row=i//2, column=i%2, sticky="w", padx=10)

    # Otros síntomas
    tk.Entry(ventana, textvariable=otros_sintomas, width=40).pack(pady=5)
    tk.Label(ventana, text="(Otros síntomas)").pack()

    # Duración
    tk.Label(ventana, text="Duración de los síntomas:").pack(pady=5)
    frame4 = tk.Frame(ventana)
    frame4.pack()
    tk.Radiobutton(frame4, text="< 24 horas", variable=duracion_var, value="<24h").pack(side="left", padx=5)
    tk.Radiobutton(frame4, text="1–3 días", variable=duracion_var, value="1-3 días").pack(side="left", padx=5)
    tk.Radiobutton(frame4, text="> 3 días", variable=duracion_var, value=">3 días").pack(side="left", padx=5)

    # Función que recogerá los datos y procesará el diagnóstico
    def diagnosticar():
        datos = {
            "especie": especie_var.get(),
            "edad": edad_var.get(),
            "sexo": sexo_var.get(),
            "esterilizado": esterilizado_var.get(),
            "sintomas": {k: v.get() for k, v in sintomas.items()},
            "otros": otros_sintomas.get(),
            "duracion": duracion_var.get()
        }

        motor = DiagnosticoVeterinario()
        motor.reset()
        motor.declare(Paciente(**datos))
        motor.run()

        # Recoger resultados del motor
        resultado = motor.resultado or "No se pudo determinar un diagnóstico."
        descripcion = getattr(motor, 'descripcion', '')
        tratamiento = getattr(motor, 'tratamiento', [])

        # Preparar mensaje
        mensaje = f"Diagnóstico: {resultado}\n"
        if descripcion:
            mensaje += f"Descripción: {descripcion}\n"
        if tratamiento:
            mensaje += "Tratamiento:\n"
            for item in tratamiento:
                mensaje += f" - {item}\n"

        # Mostrar en ventana emergente
        messagebox.showinfo("Resultado del Diagnóstico", mensaje)

        # Cargar o crear historial
        if os.path.exists("historial.json"):
            try:
                with open("historial.json", "r", encoding="utf-8") as f:
                    historial = json.load(f)
            except json.JSONDecodeError:
                historial = []
        else:
            historial = []

        # Construir entrada nueva
        entrada = {
            "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "especie": datos["especie"],
            "edad": datos["edad"],
            "sexo": datos["sexo"],
            "esterilizado": datos["esterilizado"],
            "sintomas": datos["sintomas"],
            "otros": datos["otros"],
            "duracion": datos["duracion"],
            "diagnostico": resultado,
            "descripcion": descripcion,
            "tratamiento": tratamiento
        }

        # Agregar al historial y guardar
        historial.append(entrada)
        with open("historial.json", "w", encoding="utf-8") as f:
            json.dump(historial, f, ensure_ascii=False, indent=4)

    # Botón de diagnóstico
    tk.Button(ventana, text="Diagnosticar", command=diagnosticar, bg="green", fg="white").pack(pady=15)

    # Botón: Salir
    btn_salir = tk.Button(
        ventana,
        text="Salir",
        font=("Arial", 12),
        bg="red", fg="white",
        command=lambda: [ventana.destroy(), ventana.master.destroy()]
    )
    btn_salir.pack(side="bottom", pady=10)
