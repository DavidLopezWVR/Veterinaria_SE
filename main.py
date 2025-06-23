import tkinter as tk
from presentacion import crear_ventana_presentacion
from interfaz import crear_ventana_diagnostico
from historial import mostrar_historial

class ControladorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()  # Oculta ventana raíz principal

        self.ventana_presentacion()

    def ventana_presentacion(self):
        # Crear ventana de presentación, pasar referencias para botones
        print("Abriendo presentación")
        crear_ventana_presentacion(
            iniciar_callback=self.ventana_diagnostico,
            historial_callback=self.ventana_historial
        )

    def ventana_diagnostico(self):
        crear_ventana_diagnostico()

    def ventana_historial(self):
        mostrar_historial()

if __name__ == "__main__":
    app = ControladorApp()
    tk.mainloop()
