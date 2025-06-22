import tkinter as tk
from PIL import Image, ImageTk

# Crear ventana
ventana = tk.Tk()
ventana.title("Sistema Experto Veterinario")
ventana.geometry("800x600")

# Cargar imagen de fondo
fondo_img = Image.open("img/fondo.png")
fondo_img = fondo_img.resize((800, 600))
fondo_tk = ImageTk.PhotoImage(fondo_img)

# Etiqueta para fondo
fondo_label = tk.Label(ventana, image=fondo_tk)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Cargar logo
logo_img = Image.open("img/logo.png")
logo_img = logo_img.resize((120, 120))  # Ajusta tamaño según necesidad
logo_tk = ImageTk.PhotoImage(logo_img)

# Colocar logo
logo_label = tk.Label(ventana, image=logo_tk, bg="white")
logo_label.place(x=340, y=50)  # Centrado horizontal

# Título
titulo = tk.Label(ventana, text="Bienvenido a VetExpert", font=("Arial", 20, "bold"), bg="white")
titulo.place(x=270, y=180)

# Botones
def iniciar_diagnostico():
    ventana.destroy()
    import interfaz  # Llama a la siguiente pantalla (pantalla de síntomas)

def ver_historial():
    print("Aquí puedes abrir una ventana futura para mostrar el historial...")

btn_inicio = tk.Button(ventana, text="Iniciar diagnóstico", font=("Arial", 14), bg="green", fg="white", command=iniciar_diagnostico)
btn_inicio.place(x=300, y=250, width=200, height=40)

btn_historial = tk.Button(ventana, text="Ver historial", font=("Arial", 14), bg="blue", fg="white", command=ver_historial)
btn_historial.place(x=300, y=310, width=200, height=40)

ventana.mainloop()
