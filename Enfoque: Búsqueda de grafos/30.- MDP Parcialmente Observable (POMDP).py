import random

# --- POMDP ---
# El agente no conoce el estado exacto, solo mantiene una creencia (probabilidad).

# Estados y objetivo
estados = ['A', 'B', 'C']
objetivo = 'C'

# Acciones
acciones = ['avanzar', 'quedarse']

# Transiciones con probabilidades
transiciones = {
    'A': {'avanzar': [('B', 0.8), ('A', 0.2)], 'quedarse': [('A', 1.0)]},
    'B': {'avanzar': [('C', 0.9), ('B', 0.1)], 'quedarse': [('B', 1.0)]},
    'C': {'avanzar': [('C', 1.0)], 'quedarse': [('C', 1.0)]}
}

# Observaciones y modelo P(obs|estado)
observaciones = ['cerca', 'lejos']
modelo_obs = {
    'A': {'lejos': 0.8, 'cerca': 0.2},
    'B': {'lejos': 0.3, 'cerca': 0.7},
    'C': {'lejos': 0.1, 'cerca': 0.9}
}

# Recompensas
def recompensa(s):
    return 100 if s == objetivo else -1

# Creencia inicial
belief = {'A': 0.6, 'B': 0.3, 'C': 0.1}

def actualizar_belief(belief, accion, obs):
    """Actualiza la creencia según transición y observación."""
    nuevo = {}
    for s_next in estados:
        prob = 0
        for s in estados:
            for s2, p in transiciones[s][accion]:
                if s2 == s_next:
                    prob += belief[s] * p
        prob *= modelo_obs[s_next][obs]
        nuevo[s_next] = prob
    # Normalizar
    total = sum(nuevo.values())
    for s in nuevo:
        nuevo[s] /= total
    return nuevo

def elegir_accion(belief):
    """Estrategia simple: si cree estar cerca, avanza."""
    if belief['C'] > 0.5 or belief['B'] > 0.5:
        return 'avanzar'
    return 'quedarse'

def simular(pasos=5):
    """Simula ejecución POMDP con actualización de creencias."""
    global belief
    estado_real = random.choice(estados)
    print("\n--- Simulación POMDP ---\n")

    for t in range(pasos):
        accion = elegir_accion(belief)
        # transición real
        posibles = transiciones[estado_real][accion]
        estados_siguientes = [s for s, _ in posibles]
        probs = [p for _, p in posibles]
        estado_real = random.choices(estados_siguientes, weights=probs)[0]
        # observación
        obs_probs = modelo_obs[estado_real]
        obs = random.choices(list(obs_probs.keys()), weights=obs_probs.values())[0]
        # actualizar creencia
        belief = actualizar_belief(belief, accion, obs)

        print(f"Paso {t}: Acción={accion}, Obs={obs}, Creencia={belief}")

        if estado_real == objetivo:
            print("¡Objetivo alcanzado!")
            break

# --- Ejecución ---
simular()
