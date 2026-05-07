# Definimos nuestro grafo de conexiones
# Cada nodo tiene vecinos a los que puede moverse
red_tabu = {
    'Inicio': ['X', 'Y'],
    'X': ['Inicio', 'P', 'Q'],
    'Y': ['Inicio', 'R', 'T'], 
    'P': ['X'],
    'Q': ['X', 'S'],       # 'Q' es un máximo local, su única salida nueva es 'S'
    'S': ['Q', 'T'],
    'T': ['S', 'Y'],      
    'R': ['Y', 'Meta'],
    'Meta': ['R']          # Nodo objetivo final
}

# Heurística: valores estimados de distancia hacia la meta
# Mientras más bajo sea el valor, más cerca estamos de la solución
estimacion = {
    'Inicio': 10,
    'X': 7,
    'Y': 9,     # Al inicio parece poco prometedor
    'P': 8,
    'Q': 4,     # Máximo local (trampa)
    'S': 5,     # Peor que Q
    'T': 6,     # Peor que S
    'R': 3,
    'Meta': 0   # Meta global
}

def algoritmo_tabu(red, h, inicio, objetivo, memoria=2, limite_iter=15):
    """
    Algoritmo de búsqueda tabú:
    - Evita caer en máximos locales usando una memoria de nodos prohibidos (tabú).
    - Se mueve incluso si el vecino es peor, para escapar de trampas.
    """
    print(f"--- Iniciando Búsqueda Tabú (Inicio: '{inicio}', Objetivo: '{objetivo}') ---")
    print(f"Tamaño de la memoria Tabú: {memoria}\n")
    
    nodo = inicio
    recorrido = [nodo]
    lista_tabu = []  # Memoria a corto plazo
    
    for paso in range(limite_iter):
        valor_nodo = h[nodo]
        print(f"[Iteración {paso+1}] Nodo actual: {nodo} (Valor: {valor_nodo})")
        print(f"  Memoria Tabú: {lista_tabu}")
        
        # 1. Condición de éxito
        if nodo == objetivo:
            print(f"\n¡ÉXITO! Objetivo '{objetivo}' alcanzado evitando trampas.")
            print(f"Recorrido final: {recorrido}")
            return True
            
        # 2. Obtener vecinos disponibles
        vecinos = red.get(nodo, [])
        if not vecinos:
            print("No hay más caminos disponibles. Fin de la búsqueda.")
            return False
            
        # 3. Buscar el mejor vecino que NO esté en la lista tabú
        mejor_opcion = None
        mejor_valor = float('inf')  # Queremos el valor más bajo
        
        for v in vecinos:
            if v in lista_tabu:
                print(f"    -> Vecino '{v}' es TABÚ (Ignorado)")
                continue
                
            valor_v = h.get(v, float('inf'))
            print(f"    -> Evaluando vecino '{v}' (Valor: {valor_v})")
            
            if valor_v < mejor_valor:
                mejor_valor = valor_v
                mejor_opcion = v
                
        # 4. Si todos los vecinos son tabú, no hay salida
        if mejor_opcion is None:
            print("\nTodos los caminos están bloqueados por la memoria Tabú. Fin de la búsqueda.")
            return False
            
        # 5. Avanzamos, incluso si el vecino es peor que el nodo actual
        if mejor_valor > valor_nodo:
            print(f"  [*] Decisión arriesgada: empeoramos de {valor_nodo} a {mejor_valor} para escapar.")
            
        # Actualizamos la memoria tabú con el nodo que dejamos atrás
        lista_tabu.append(nodo)
        if len(lista_tabu) > memoria:
            lista_tabu.pop(0)  # Olvidamos el más antiguo
            
        # Movemos al mejor vecino
        nodo = mejor_opcion
        recorrido.append(nodo)
        print("-" * 40)
        
    print(f"\nSe alcanzó el límite de iteraciones ({limite_iter}) sin llegar al objetivo.")
    return False

# --- PRUEBA DEL CÓDIGO ---
algoritmo_tabu(red_tabu, estimacion, inicio='Inicio', objetivo='Meta', memoria=2)
