# presentacion.py
import tkinter as tk
from PIL import Image, ImageTk

def crear_ventana_presentacion(iniciar_callback, historial_callback):
    # Abrimos una ventana Toplevel (no Tk) para integrarse con main.py
    ventana = tk.Toplevel()
    ventana.title("Sistema Experto Veterinario")
    ventana.geometry("800x600")

    # --- FUSIÓN DEL LOGO SOBRE EL FONDO ---
    # Ruta relativa a tu proyecto: asegúrate de que exista "img/fondo_1.jpg" y "img/logo.png"
    fondo = Image.open("img/fondo_1.jpg").resize((800, 600)).convert("RGBA")
    logo  = Image.open("img/logo.png").convert("RGBA").resize((400, 240))
    fondo.paste(logo, (200, 50), mask=logo)

    # Convertir la imagen combinada y mantener la referencia
    fondo_tk = ImageTk.PhotoImage(fondo)
    fondo_label = tk.Label(ventana, image=fondo_tk)
    fondo_label.image = fondo_tk        # ← Muy importante para que no lo borre el GC
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    # --- INTERFAZ GRÁFICA SOBRE EL FONDO ---
    titulo = tk.Label(
        ventana,
        text="Bienvenido a DoctorineExpert",
        font=("Arial", 20, "bold"),
        bg="white"
    )
    titulo.place(x=210, y=320)

    # Botón: Iniciar diagnóstico
    btn_inicio = tk.Button(
        ventana,
        text="Iniciar diagnóstico",
        font=("Arial", 14),
        bg="green", fg="white",
        command=lambda: [ventana.destroy(), iniciar_callback()]
    )
    btn_inicio.place(x=300, y=370, width=200, height=40)

    # Botón: Ver historial
    btn_historial = tk.Button(
        ventana,
        text="Ver historial",
        font=("Arial", 14),
        bg="blue", fg="white",
        command=lambda: [ventana.destroy(), historial_callback()]
    )
    btn_historial.place(x=300, y=430, width=200, height=40)

    # Botón: Salir
    btn_salir = tk.Button(
        ventana,
        text="Salir",
        font=("Arial", 14),
        bg="red", fg="white",
        command=lambda: [ventana.destroy(), ventana.master.destroy()]
    )
    btn_salir.place(x=300, y=490, width=200, height=40)


    # ¡OJO! No se llama a ventana.mainloop() aquí,
    # el bucle principal viene de main.py
