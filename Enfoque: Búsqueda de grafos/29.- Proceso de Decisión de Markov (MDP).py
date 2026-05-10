import random

# --- MDP y Q-Learning ---
# El entorno es aleatorio y controlado por el agente.
# Q-Learning aprende valores estado-acción sin conocer reglas previas.

# Estados y acciones
zonas = ['Base', 'Ruta_Nevada', 'Punto_Extracción', 'Grieta']
maniobras = ['Avanzar', 'Esperar']
finales = ['Punto_Extracción', 'Grieta']

def entorno(ubicacion, accion):
    """Simula transición con azar y recompensa."""
    if ubicacion == 'Base':
        if accion == 'Avanzar':
            return ('Ruta_Nevada', -1) if random.random() < 0.9 else ('Base', -1)
        return 'Base', -1
    elif ubicacion == 'Ruta_Nevada':
        if accion == 'Avanzar':
            return ('Punto_Extracción', 100) if random.random() < 0.7 else ('Grieta', -100)
        return 'Base', -1
    return ubicacion, 0

# Tabla Q inicial
Q = {z: {m: 0.0 for m in maniobras} for z in zonas}

# Parámetros
alpha = 0.1   # tasa de aprendizaje
gamma = 0.9   # descuento futuro
epsilon = 0.2 # exploración
episodios = 2000

print("--- Entrenando con Q-Learning ---")

for ep in range(1, episodios + 1):
    estado = 'Base'
    while estado not in finales:
        # Decisión: explorar o explotar
        if random.random() < epsilon:
            accion = random.choice(maniobras)
        else:
            accion = max(Q[estado], key=Q[estado].get)

        # Interacción con entorno
        nuevo_estado, recompensa = entorno(estado, accion)

        # Actualización Q: TD
        max_futuro = max(Q[nuevo_estado].values()) if nuevo_estado not in finales else 0.0
        viejo = Q[estado][accion]
        objetivo = recompensa + gamma * max_futuro
        Q[estado][accion] = viejo + alpha * (objetivo - viejo)

        estado = nuevo_estado

    if ep % 500 == 0:
        print(f" > Episodio {ep} completado.")

# --- Resultados ---
print("\n--- Tabla Q Final ---")
for z in ['Base', 'Ruta_Nevada']:
    print(f"{z}:")
    for m, val in Q[z].items():
        print(f"  {m}: {val:.2f}")

print("\n--- Política Aprendida ---")
for z in ['Base', 'Ruta_Nevada']:
    mejor = max(Q[z], key=Q[z].get)
    print(f"En {z} -> {mejor.upper()}")
