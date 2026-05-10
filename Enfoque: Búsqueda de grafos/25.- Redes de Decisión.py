# --- Red de Decisión ---
# Ejemplo: decidir si llevar paraguas según utilidad esperada.

# Probabilidades de clima
P_lluvia = 0.3
P_no_lluvia = 0.7

# Utilidades de cada acción según el clima
utilidades = {
    'llevar': {
        'lluvia': 50,     # protegido
        'no_lluvia': -10  # incomodidad
    },
    'no_llevar': {
        'lluvia': -100,   # se moja
        'no_lluvia': 20   # cómodo
    }
}

def utilidad_esperada(accion):
    """Calcula utilidad esperada combinando probabilidad y resultado."""
    return (
        P_lluvia * utilidades[accion]['lluvia'] +
        P_no_lluvia * utilidades[accion]['no_lluvia']
    )

def tomar_decision():
    """Evalúa acciones y elige la de mayor utilidad esperada."""
    acciones = ['llevar', 'no_llevar']
    resultados = {a: utilidad_esperada(a) for a in acciones}

    print("\nUtilidades esperadas:")
    for a, v in resultados.items():
        print(f"{a}: {v:.2f}")

    mejor = max(resultados, key=resultados.get)
    print("\nMejor decisión:", mejor)

# --- Ejecución ---
tomar_decision()
