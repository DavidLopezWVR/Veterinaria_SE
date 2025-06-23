# Sistema Experto Veterinario

Este proyecto implementa un **Sistema Experto** para apoyar el diagnóstico primario de animales (perros y gatos) en una clínica veterinaria. Utiliza una interfaz gráfica con **Tkinter**, un motor de reglas con la librería **experta** y una base de conocimiento externalizada en **JSON**.

## Características

- **Interfaz gráfica** con ventanas para bienvenida, diagnóstico y visualización del historial.
- **Base de conocimiento** en `conocimiento.json`, editable y ampliable.
- **Motor de inferencia** que genera reglas dinámicamente a partir del JSON.
- **Persistencia** de diagnósticos en `historial.json`.
- **Controlador central** (`main.py`) que gestiona el flujo de la aplicación.
- **Entorno virtual** para aislar dependencias (`venv/`).

## Requisitos

- Python 3.9
- Paquetes:
  - `experta`
  - `Pillow`

## Instalación

```bash
git clone <URL_DEL_REPOSITORIO>
cd Veterinaria_SE
python3.9 -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
```

## Estructura del proyecto

```
Veterinaria_SE/
├── conocimiento.json         # Base de conocimiento en JSON
├── conocimiento.py           # Módulo para cargar el JSON
├── reglas.py                 # Motor de inferencia dinámico
├── presentacion.py           # Pantalla de bienvenida
├── interfaz.py               # Ventana de ingreso y diagnóstico
├── historial.py              # Ventana de historial
├── main.py                   # Controlador central
├── historial.json            # Historial generado (JSON)
├── requirements.txt          # Lista de dependencias
└── img/
    ├── fondo_1.jpg
    └── logo.png
```

## Uso

```bash
python main.py
```

1. Pantalla de bienvenida:
   - **Iniciar diagnóstico**
   - **Ver historial**
   - **Salir**
2. Ventana de diagnóstico:
   - Ingresar datos del paciente (especie, edad, sexo, etc.)
   - Seleccionar síntomas y duración
   - Pulsar **Diagnosticar** para ver resultados
   - Pulsar **Salir** para cerrar la aplicación
3. Ventana de historial:
   - Navegar por diagnósticos previos
   - Pulsar **Salir** para cerrar

## Personalización

- **Añadir síntomas**: Editar la lista `"sintomas"` en `conocimiento.json`.
- **Agregar enfermedades**: Añadir objetos en la sección `"enfermedades"` de `conocimiento.json`.

## License

Proyecto libre para uso académico y personal.
