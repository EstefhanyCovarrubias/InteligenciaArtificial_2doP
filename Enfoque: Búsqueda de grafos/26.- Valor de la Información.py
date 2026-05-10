# --- Valor de la Información (VOI) ---
# Compara decisiones sin información vs con información perfecta.

# Probabilidades
P_lluvia = 0.3
P_no_lluvia = 0.7

# Utilidades según acción y clima
utilidades = {
    'llevar': {'lluvia': 50, 'no_lluvia': -10},
    'no_llevar': {'lluvia': -100, 'no_lluvia': 20}
}

def utilidad_esperada(accion):
    """Calcula utilidad esperada combinando probabilidad y resultado."""
    return (
        P_lluvia * utilidades[accion]['lluvia'] +
        P_no_lluvia * utilidades[accion]['no_lluvia']
    )

def mejor_sin_info():
    """Evalúa acciones sin información adicional."""
    acciones = ['llevar', 'no_llevar']
    resultados = {a: utilidad_esperada(a) for a in acciones}
    mejor = max(resultados, key=resultados.get)
    return mejor, resultados[mejor], resultados

def con_info_perfecta():
    """Evalúa decisiones con información perfecta del clima."""
    mejor_lluvia = 'llevar' if utilidades['llevar']['lluvia'] > utilidades['no_llevar']['lluvia'] else 'no_llevar'
    mejor_no_lluvia = 'llevar' if utilidades['llevar']['no_lluvia'] > utilidades['no_llevar']['no_lluvia'] else 'no_llevar'

    utilidad_total = (
        P_lluvia * utilidades[mejor_lluvia]['lluvia'] +
        P_no_lluvia * utilidades[mejor_no_lluvia]['no_lluvia']
    )
    return mejor_lluvia, mejor_no_lluvia, utilidad_total

def calcular_voi():
    """Compara utilidad sin info vs con info y calcula VOI."""
    mejor_accion, sin_info, resultados = mejor_sin_info()
    decision_lluvia, decision_no_lluvia, con_info = con_info_perfecta()
    voi = con_info - sin_info

    print("\n--- SIN INFORMACIÓN ---")
    for a, v in resultados.items():
        print(f"{a}: {v:.2f}")
    print("Mejor decisión:", mejor_accion, "| Utilidad:", sin_info)

    print("\n--- CON INFORMACIÓN PERFECTA ---")
    print(f"Si llueve → {decision_lluvia}")
    print(f"Si no llueve → {decision_no_lluvia}")
    print("Utilidad esperada:", con_info)

    print("\n--- VALOR DE LA INFORMACIÓN ---")
    print("VOI:", voi)

# --- Ejecución ---
calcular_voi()
