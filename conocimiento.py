# conocimiento.py
import json, os

def cargar_conocimiento(ruta="conocimiento.json"):
    # Obtiene la carpeta donde está este archivo
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, ruta)

    if not os.path.exists(path):
        raise FileNotFoundError(f"No se encontró {path}")
    with open(path, encoding="utf-8") as f:
        return json.load(f)

KB = cargar_conocimiento()
