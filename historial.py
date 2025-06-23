# historial.py
import tkinter as tk
import json
import os

def mostrar_historial():
    ventana = tk.Toplevel()
    ventana.title("Historial de Diagnósticos")
    ventana.geometry("800x600")

    # Área de texto para mostrar el historial
    texto = tk.Text(ventana, wrap="word", font=("Arial", 12))
    texto.pack(expand=True, fill="both", padx=10, pady=10)

    # Leer historial
    if os.path.exists("historial.json"):
        with open("historial.json", "r", encoding="utf-8") as f:
            historial = json.load(f)

        if historial:
            for caso in historial:
                texto.insert("end", f"Fecha: {caso['fecha']}\n")
                texto.insert("end", f"Especie: {caso['especie']} | Edad: {caso['edad']} años | Sexo: {caso['sexo']} | Esterilizado: {caso['esterilizado']}\n")
                texto.insert("end", f"Duración síntomas: {caso['duracion']}\n")
                texto.insert("end", "Síntomas:\n")
                for sintoma, presente in caso["sintomas"].items():
                    if presente:
                        texto.insert("end", f"  - {sintoma.replace('_', ' ')}\n")
                if caso["otros"]:
                    texto.insert("end", f"Otros síntomas: {caso['otros']}\n")
                texto.insert("end", f"Diagnóstico: {caso['diagnostico']}\n")
                texto.insert("end", "-"*60 + "\n\n")
        else:
            texto.insert("end", "El historial está vacío.")
    else:
        texto.insert("end", "No se encontró el archivo historial.json.")

    # Botón: Salir
    btn_salir = tk.Button(
        ventana,
        text="Salir",
        font=("Arial", 12),
        bg="red", fg="white",
        command=lambda: [ventana.destroy(), ventana.master.destroy()]
    )
    btn_salir.pack(side="bottom", pady=10)

