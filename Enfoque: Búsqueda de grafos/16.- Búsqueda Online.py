# --- 1. EL MUNDO REAL (El agente no conoce este mapa directamente) ---
# Solo puede descubrir vecinos cuando está físicamente en un nodo.
mapa_real = {
    'X': ['Y', 'Z'],
    'Y': ['W'],
    'Z': ['V'],
    'W': ['Objetivo'],
    'V': ['Objetivo'],
    'Objetivo': []
}

# --- 2. LA MEMORIA DEL AGENTE (Tabla heurística H) ---
tabla_H = {
    'X': 1, 'Y': 1, 'Z': 1,
    'W': 1, 'V': 1, 'Objetivo': 0
}

# --- Función que simula los sensores del agente ---
def sensores(nodo):
    """El agente observa qué caminos salen del nodo actual."""
    return mapa_real.get(nodo, [])

# --- Algoritmo LRTA* (Learning Real-Time A*) ---
def lrta_busqueda(origen, destino):
    print(f"--- Iniciando LRTA* desde '{origen}' ---")
    
    posicion = origen
    recorrido = [posicion]  # Camino físico recorrido
    
    while posicion != destino:
        print(f"\n[Estoy en]: {posicion} | Estimación H({posicion}) = {tabla_H[posicion]}")
        
        # 1. Observar vecinos visibles con sensores
        vecinos = sensores(posicion)
        if not vecinos:
            print("Error: atrapado sin salida.")
            return False
            
        print(f"  -> Sensores detectan: {vecinos}")
        
        # 2. Evaluar vecinos con f(s') = costo + H(s')
        mejor_opcion = None
        mejor_valor = float('inf')
        
        for vecino in vecinos:
            h_valor = tabla_H.get(vecino, 1)  # Si no está en memoria, asumimos 1
            costo = 1
            f_valor = costo + h_valor
            print(f"     * Evalúo '{vecino}': Costo(1) + H({vecino})={h_valor} → f={f_valor}")
            
            if f_valor < mejor_valor:
                mejor_valor = f_valor
                mejor_opcion = vecino
                
        # 3. Aprendizaje: actualizar la heurística del nodo actual
        if tabla_H[posicion] != mejor_valor:
            print(f"  [Aprendizaje] Actualizo H({posicion}) de {tabla_H[posicion]} a {mejor_valor}")
            tabla_H[posicion] = mejor_valor
            
        # 4. Moverse físicamente al mejor vecino
        print(f"  >> Avanzando hacia '{mejor_opcion}'...")
        posicion = mejor_opcion
        recorrido.append(posicion)
        
    print(f"\n¡META ALCANZADA! '{destino}' encontrado.")
    print(f"Recorrido físico: {recorrido}")
    print(f"Tabla heurística final: {tabla_H}")
    return True

# --- PRUEBA DEL CÓDIGO ---
lrta_busqueda('X', 'Objetivo')
