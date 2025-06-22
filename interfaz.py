import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Sistema Experto Veterinario")
ventana.geometry("600x600")

# Variables
especie_var = tk.StringVar(value="Perro")
sexo_var = tk.StringVar(value="Macho")
esterilizado_var = tk.StringVar(value="Sí")
edad_var = tk.StringVar()

# Síntomas
sintomas = {
    "fiebre": tk.BooleanVar(),
    "vomito": tk.BooleanVar(),
    "diarrea": tk.BooleanVar(),
    "tos": tk.BooleanVar(),
    "letargo": tk.BooleanVar(),
    "falta_apetito": tk.BooleanVar(),
    "secrecion_nasal": tk.BooleanVar(),
}
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

# Función que recogerá los datos (conectará al SE después)
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
    print("Datos recopilados:", datos)  # Aquí después se llamará al motor de reglas

# Botón de diagnóstico
tk.Button(ventana, text="Diagnosticar", command=diagnosticar, bg="green", fg="white").pack(pady=15)

ventana.mainloop()
