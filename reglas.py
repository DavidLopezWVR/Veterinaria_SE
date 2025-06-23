# reglas.py
from experta import KnowledgeEngine, Fact, Rule, MATCH, P
from conocimiento import KB

class Paciente(Fact):
    """Hechos sobre el paciente"""
    pass

def generar_regla(enfermedad):
    """
    Devuelve un método para la regla que activa cuando
    todos los síntomas del patrón están presentes.
    """
    patron = set(enfermedad["patron"])
    nombre = enfermedad["nombre"]
    desc = enfermedad["descripcion"]
    trat = enfermedad["tratamiento"]

    @Rule(
        Paciente(
            sintomas= MATCH.s 
            & P(lambda s, patron=patron: patron.issubset({k for k,v in s.items() if v}))
        )
    )
    def regla(self):
        self.resultado     = nombre
        self.descripcion  = desc
        self.tratamiento  = trat

    return regla

class DiagnosticoVeterinario(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.resultado    = ""
        self.descripcion  = ""
        self.tratamiento  = []

# ——— Registrar dinámicamente todas las reglas ———
for enfer in KB["enfermedades"]:
    metodo = generar_regla(enfer)
    setattr(
        DiagnosticoVeterinario,
        f"regla_{enfer['nombre'].lower().replace(' ', '_')}",
        metodo
    )

# Regla “catch-all” para síntomas no reconocidos
@Rule(Paciente(sintomas=MATCH.s & P(lambda s: any(s.values()) and not any(
    set(enf["patron"]).issubset({k for k,v in s.items() if v})
    for enf in KB["enfermedades"]
))))
def diagnostico_indeterminado(self):
    self.resultado    = "Síntomas no coincidentes"
    self.descripcion  = "No hay un patrón exacto, consulte al veterinario."
    self.tratamiento  = []
setattr(DiagnosticoVeterinario, "diagnostico_indeterminado", diagnostico_indeterminado)

# Regla para “sin síntomas”
@Rule(Paciente(sintomas=MATCH.s & P(lambda s: all(not v for v in s.values()))))
def sin_sintomas(self):
    self.resultado   = "Paciente sin síntomas"
    self.descripcion = "El paciente parece estable."
    self.tratamiento = []
setattr(DiagnosticoVeterinario, "sin_sintomas", sin_sintomas)
