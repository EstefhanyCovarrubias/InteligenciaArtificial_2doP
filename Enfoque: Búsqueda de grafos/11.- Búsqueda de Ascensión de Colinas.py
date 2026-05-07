# Definimos un grafo AND/OR donde cada nodo puede ser:
# - OR: se puede elegir entre sus hijos
# - AND: se deben cumplir todos sus hijos
tareas = {
    'Inicio': {'tipo': 'OR',  'hijos': ['Plan_A', 'Plan_B']},   # Inicio puede resolverse con Plan_A o Plan_B
    'Plan_A': {'tipo': 'AND', 'hijos': ['Sub1', 'Sub2']},       # Plan_A requiere completar Sub1 y Sub2
    'Plan_B': {'tipo': 'OR',  'hijos': ['Sub3']},               # Plan_B se resuelve con Sub3
    # Nodos terminales (tareas básicas sin hijos)
    'Sub1': {'tipo': 'OR', 'hijos': []},                        # Sub1 es hoja
    'Sub2': {'tipo': 'OR', 'hijos': []},                        # Sub2 es hoja
    'Sub3': {'tipo': 'OR', 'hijos': []}                         # Sub3 es hoja
}

# Heurística: costo estimado de cada tarea individual
# Valores bajos = tareas más fáciles/baratas
costos_estimados = {
    'Inicio': 10, 'Plan_A': 7, 'Plan_B': 6, 
    'Sub1': 2, 'Sub2': 4, 'Sub3': 5
}

def ao_estrella(grafo, h, nodo):
    """
    Función recursiva que calcula el costo de resolver un nodo en un grafo AND/OR.
    - Si el nodo es hoja, devuelve su costo directo.
    - Si es AND, suma los costos de todos sus hijos.
    - Si es OR, toma el costo mínimo entre sus hijos.
    """

    # Obtenemos la información del nodo actual
    info = grafo.get(nodo, {'tipo': 'OR', 'hijos': []})
    
    # Caso base: nodo terminal (sin hijos)
    if not info['hijos']:
        print(f"[Hoja] '{nodo}' completado con costo {h[nodo]}")
        return h[nodo]
    
    # Si el nodo tiene hijos, los evaluamos recursivamente
    print(f"Analizando nodo '{nodo}' (Tipo: {info['tipo']})")
    costos_hijos = []
    
    for hijo in info['hijos']:
        # Llamada recursiva para calcular el costo de cada hijo
        costos_hijos.append(ao_estrella(grafo, h, hijo))
    
    # Si el nodo es AND: se deben resolver todos los hijos
    if info['tipo'] == 'AND':
        costo_total = sum(costos_hijos) + 1  # +1 por el esfuerzo de combinar
        print(f" -> '{nodo}' (AND) requiere todos sus hijos. Costo: {costo_total}")
        return costo_total
    
    # Si el nodo es OR: basta con elegir el hijo más barato
    elif info['tipo'] == 'OR':
        costo_total = min(costos_hijos) + 1  # +1 por el esfuerzo de elegir
        print(f" -> '{nodo}' (OR) toma la mejor opción. Costo: {costo_total}")
        return costo_total

# Ejecución del algoritmo AO*
print("--- Iniciando resolución con AO* ---")
costo_final = ao_estrella(tareas, costos_estimados, 'Inicio')
print(f"\nCosto óptimo total para resolver 'Inicio': {costo_final}")
