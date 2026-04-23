import random
# EXPLORACIÓN: elegimos un camino al azar
# EXPLOTACIÓN: elegimos el mejor conocido (mayor Q)
# Cada nodo tiene vecinos con una recompensa asociada
grafo = {
    'A': {'B': 1, 'C': 5},
    'B': {'D': 2, 'E': 4},
    'C': {'F': 3},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

# ==============================
# PARÁMETROS DEL ALGORITMO
# ==============================
epsilon = 0.3  # Probabilidad de exploración (30%)
episodios = 10  # Número de intentos

# Inicializamos los valores Q (qué tan buena es cada acción)
Q = {}
for nodo in grafo:
    Q[nodo] = {}
    for vecino in grafo[nodo]:
        Q[nodo][vecino] = 0  # Inicialmente no sabemos nada

# ==============================
# FUNCIÓN PARA ELEGIR ACCIÓN
# ==============================
def elegir_accion(nodo):

    if random.uniform(0, 1) < epsilon:
        # EXPLORACIÓN = probar caminos nuevos
        return random.choice(list(grafo[nodo].keys()))
    else:
        # EXPLOTACIÓN = usar el mejor camino conocido
        return max(Q[nodo], key=Q[nodo].get)

# ==============================
for episodio in range(episodios):
    nodo_actual = 'A'  # Siempre empezamos en A
    print(f"\nEpisodio {episio+1}")

    while grafo[nodo_actual]:  # Mientras haya vecinos
        accion = elegir_accion(nodo_actual)
        recompensa = grafo[nodo_actual][accion]

        # ==============================
        # ACTUALIZACIÓN SIMPLE DE Q
        # ==============================
        # Aquí actualizamos el valor del camino
        Q[nodo_actual][accion] = Q[nodo_actual][accion] + 0.1 * (recompensa - Q[nodo_actual][accion])

        print(f"{nodo_actual} -> {accion} | recompensa: {recompensa}")

        nodo_actual = accion  # Avanzamos en el grafo

print("\nValores Q aprendidos:")
for nodo in Q:
    print(nodo, Q[nodo])