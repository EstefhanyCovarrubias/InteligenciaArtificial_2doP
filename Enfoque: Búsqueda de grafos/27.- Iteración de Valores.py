import copy

# --- Iteración de Valores ---
# Algoritmo de RL que calcula utilidad de estados usando la ecuación de Bellman.

# Estados y recompensas
estados = ['Entrada', 'Plataforma_Hielo', 'Cámara_Tesoro', 'Abismo']
recompensas = {
    'Entrada': -1.0,
    'Plataforma_Hielo': -2.0,
    'Cámara_Tesoro': 100.0,
    'Abismo': -100.0
}
finales = ['Cámara_Tesoro', 'Abismo']
acciones = ['Avanzar', 'Retroceder']

# Transiciones con probabilidades
transiciones = {
    'Entrada': {
        'Avanzar': [(0.9, 'Plataforma_Hielo'), (0.1, 'Entrada')],
        'Retroceder': [(1.0, 'Entrada')]
    },
    'Plataforma_Hielo': {
        'Avanzar': [(0.7, 'Cámara_Tesoro'), (0.3, 'Abismo')],
        'Retroceder': [(1.0, 'Entrada')]
    }
}

# Parámetros
gamma = 0.9    # descuento futuro
epsilon = 0.01 # precisión

def iteracion_valores():
    """Calcula utilidades de estados con Bellman hasta convergencia."""
    U = {s: 0.0 for s in estados}
    paso = 0

    print("--- Iniciando cálculo de utilidades ---")

    while True:
        U_nueva = copy.deepcopy(U)
        delta = 0

        for s in estados:
            if s in finales:
                U_nueva[s] = recompensas[s]
                continue

            # Mejor acción según utilidad esperada
            mejor = float('-inf')
            for a in acciones:
                valor = sum(p * U[d] for p, d in transiciones[s][a])
                mejor = max(mejor, valor)

            # Bellman: U(s) = R(s) + γ * max(EU)
            U_nueva[s] = recompensas[s] + gamma * mejor
            delta = max(delta, abs(U_nueva[s] - U[s]))

        U = U_nueva
        paso += 1

        if delta < epsilon:
            print(f"[*] Convergencia en {paso} iteraciones.")
            break

    return U

# --- Ejecución ---
utilidades = iteracion_valores()

print("\n--- Utilidades finales ---")
for s, v in utilidades.items():
    print(f"{s}: {v:.2f}")

print("\n--- Política óptima ---")
for s in estados:
    if s in finales: continue
    mejor_accion = max(acciones, key=lambda a: sum(p * utilidades[d] for p, d in transiciones[s][a]))
    print(f"En {s}: elegir {mejor_accion}")
