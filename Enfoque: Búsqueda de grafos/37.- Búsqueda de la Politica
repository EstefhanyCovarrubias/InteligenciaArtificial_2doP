import random

# Cada nodo tiene vecinos con recompensas
grafo = {
    'A': {'B': 1, 'C': 5},
    'B': {'D': 2, 'E': 4},
    'C': {'F': 10},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

# ==============================
# INICIALIZACIÓN DE LA POLÍTICA
# ==============================
# La política π(nodo) = acción (a qué vecino ir)
# Se inicializa aleatoriamente
politica = {}
for nodo in grafo:
    if grafo[nodo]:
        politica[nodo] = random.choice(list(grafo[nodo].keys()))

# ==============================
# FUNCIÓN PARA EVALUAR POLÍTICA
# ==============================
def evaluar_politica():
    """
    Ejecuta la política actual desde el nodo inicial 'A'
    y suma las recompensas obtenidas.
    Esto mide qué tan buena es la política.
    """
    nodo_actual = 'A'
    recompensa_total = 0

    while grafo[nodo_actual]:
        accion = politica[nodo_actual]
        recompensa = grafo[nodo_actual][accion]

        recompensa_total += recompensa
        nodo_actual = accion

    return recompensa_total

# ==============================
# BÚSQUEDA DE LA POLÍTICA
# ==============================
# Idea clave:
# Probar pequeñas modificaciones a la política
# y quedarnos con la que da mejor recompensa
mejor_recompensa = evaluar_politica()

for iteracion in range(20):

    # Copiamos la política actual (para probar cambios)
    nueva_politica = politica.copy()

    # ==============================
    # EXPLORACIÓN EN POLÍTICAS
    # ==============================
    # Elegimos un nodo al azar y cambiamos su acción
    nodo_cambio = random.choice(list(grafo.keys()))
    if grafo[nodo_cambio]:
        nueva_politica[nodo_cambio] = random.choice(list(grafo[nodo_cambio].keys()))

    # Evaluamos la nueva política
    recompensa_nueva = 0
    nodo_actual = 'A'

    while grafo[nodo_actual]:
        accion = nueva_politica[nodo_actual]
        recompensa = grafo[nodo_actual][accion]

        recompensa_nueva += recompensa
        nodo_actual = accion

    # Si la nueva política es mejor, la adoptamos
    if recompensa_nueva > mejor_recompensa:
        politica = nueva_politica
        mejor_recompensa = recompensa_nueva

    print(f"Iteración {iteracion+1} | Mejor recompensa: {mejor_recompensa}")

print("\nPolítica óptima aproximada:")
for nodo in politica:
    print(f"{nodo} -> {politica[nodo]}")