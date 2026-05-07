#Búsquedas A
# Definimos el grafo bidireccional (cada nodo tiene conexiones con otros)
red_nodos = {
    'X': ['Y', 'Z'], 'Y': ['X', 'W', 'V'], 'Z': ['X', 'U'],
    'W': ['Y', 'T', 'S'], 'V': ['Y', 'R'], 'U': ['Z', 'Q', 'P'],
    'T': ['W', 'O'], 'S': ['W'], 'R': ['V', 'N', 'M'],
    'Q': ['U'], 'P': ['U', 'L'], 'O': ['T', 'K'],
    'N': ['R'], 'M': ['R', 'J'], 'L': ['P'],
    'K': ['O'], 'J': ['M', 'I'], 'I': ['J']
}

# Heurística: valores estimados de distancia hacia el nodo destino 'I'
# Estos valores ayudan a guiar la búsqueda A* hacia la meta.
estimacion = {
    'I': 0, 'J': 1, 'M': 2, 'N': 2, 'R': 3, 'V': 4,
    'Y': 5, 'X': 6, 'W': 6, 'Z': 7, 'T': 7, 'S': 7,
    'U': 8, 'O': 8, 'Q': 9, 'P': 9, 'K': 9, 'L': 10
}

def algoritmo_a_estrella(red, h, inicio, destino):
    print(f"--- Iniciando Algoritmo A* (Inicio: {inicio}, Destino: {destino}) ---")
    
    # Inicializamos la cola con el nodo de inicio
    # g = costo real acumulado (inicialmente 0)
    # f = g + h (heurística)
    g_inicio = 0
    f_inicio = g_inicio + h[inicio]
    cola = [(f_inicio, g_inicio, inicio, [inicio])]
    
    # Conjunto de nodos ya explorados
    explorados = set()

    # Mientras haya nodos en la cola
    while cola:
        # Ordenamos la cola por f(n) (el valor más prometedor primero)
        cola.sort(key=lambda x: x[0])
        
        # Extraemos el nodo con menor f(n)
        f_actual, g_actual, nodo_actual, camino = cola.pop(0)
        
        print(f"Evaluando: {nodo_actual} (Costo real g={g_actual}, Estimación h={h[nodo_actual]} -> f={f_actual})")

        # Si llegamos al destino, terminamos
        if nodo_actual == destino:
            print(f"\n¡ÉXITO! Destino '{destino}' encontrado con la ruta más corta garantizada.")
            print(f"Ruta A*: {camino}")
            print(f"Costo total del viaje: {g_actual}")
            return True

        # Si el nodo no ha sido explorado, lo marcamos y expandimos sus vecinos
        if nodo_actual not in explorados:
            explorados.add(nodo_actual)
            
            for vecino in red.get(nodo_actual, []):
                if vecino not in explorados:
                    # Cada paso cuesta 1 en este ejemplo
                    g_vecino = g_actual + 1
                    h_vecino = h.get(vecino, float('inf'))  # heurística del vecino
                    f_vecino = g_vecino + h_vecino          # cálculo de f(n)
                    
                    # Agregamos el vecino a la cola con su camino acumulado
                    cola.append((f_vecino, g_vecino, vecino, camino + [vecino]))
                    
    # Si la cola se vacía y no encontramos el destino
    return False

# Ejecutamos el algoritmo desde 'X' hasta 'I'
algoritmo_a_estrella(red_nodos, estimacion, inicio='X', destino='I')
