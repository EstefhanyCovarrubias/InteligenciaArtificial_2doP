# --- Teoría de la Utilidad ---
# Decisiones se toman según la utilidad esperada de cada acción.

# Opciones: cada acción tiene resultados (probabilidad, utilidad)
opciones = {
    'Invertir': [
        (0.7, 100),   # gana dinero
        (0.3, -50)    # pierde dinero
    ],
    'Ahorrar': [
        (1.0, 30)     # ganancia segura
    ],
    'Gastar': [
        (1.0, 60)     # satisfacción inmediata
    ]
}

def utilidad(x):
    """Convierte resultado en utilidad (ejemplo: aversión al riesgo)."""
    if x >= 0:
        return x ** 0.5   # utilidad positiva
    else:
        return -((-x) ** 0.5)  # utilidad negativa

def utilidad_esperada(opcion):
    """Calcula utilidad esperada: suma de prob*utilidad."""
    total = 0
    for prob, resultado in opcion:
        total += prob * utilidad(resultado)
    return total

def elegir_mejor(opciones):
    """Evalúa todas las acciones y elige la de mayor utilidad esperada."""
    resultados = {}
    for nombre, opcion in opciones.items():
        resultados[nombre] = utilidad_esperada(opcion)

    print("\nUtilidades esperadas:")
    for op, val in resultados.items():
        print(f"{op}: {val:.4f}")

    mejor = max(resultados, key=resultados.get)
    print("\nMejor decisión:", mejor)

# --- Ejecución ---
elegir_mejor(opciones)
