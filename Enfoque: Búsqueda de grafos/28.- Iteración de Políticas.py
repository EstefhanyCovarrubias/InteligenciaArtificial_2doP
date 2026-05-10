# --- Iteración de Políticas ---
# Alterna entre evaluar la política actual y mejorarla hasta que sea óptima.

# Estados y recompensas
puntos = ['Hangar', 'Pista_Hielo', 'Meta', 'Colisión']
premios = {'Hangar': -1, 'Pista_Hielo': -1, 'Meta': 100, 'Colisión': -100}
terminales = ['Meta', 'Colisión']
maniobras = ['Avanzar', 'Esperar']

# Transiciones con probabilidades
fisica_vuelo = {
    'Hangar': {
        'Avanzar': [(0.9, 'Pista_Hielo'), (0.1, 'Hangar')],
        'Esperar': [(1.0, 'Hangar')]
    },
    'Pista_Hielo': {
        'Avanzar': [(0.7, 'Meta'), (0.3, 'Colisión')],
        'Esperar': [(1.0, 'Hangar')]
    }
}

gamma = 0.9  # descuento futuro

def evaluar_manual(manual, valores):
    """Evalúa la política actual calculando valores de estados."""
    for _ in range(15):  # iteraciones para estabilizar
        nuevos = valores.copy()
        for s in puntos:
            if s in terminales:
                nuevos[s] = premios[s]
                continue
            accion = manual[s]
            eu = sum(p * valores[d] for p, d in fisica_vuelo[s][accion])
            nuevos[s] = premios[s] + gamma * eu
        valores = nuevos
    return valores

def optimizar_navegacion():
    """Mejora la política hasta que sea estable."""
    print("--- Entrenamiento de Política ---")
    manual = {s: 'Esperar' for s in puntos if s not in terminales}
    valores = {s: 0.0 for s in puntos}
    ciclo = 1

    while True:
        print(f"\n[Ciclo {ciclo}] Política actual: {manual}")
        valores = evaluar_manual(manual, valores)

        estable = True
        for s in puntos:
            if s in terminales: continue
            mejor = max(maniobras, key=lambda m: sum(p * valores[d] for p, d in fisica_vuelo[s][m]))
            if mejor != manual[s]:
                manual[s] = mejor
                estable = False
                print(f"  Ajuste en {s}: nueva acción -> {mejor}")

        if estable:
            print("\n[✔] Política óptima encontrada.")
            break
        ciclo += 1

    return manual, valores

# --- Ejecución ---
estrategia, valores_finales = optimizar_navegacion()

print("\n--- Política Final ---")
for s in ['Hangar', 'Pista_Hielo']:
    print(f"{s}: {estrategia[s].upper()}")
