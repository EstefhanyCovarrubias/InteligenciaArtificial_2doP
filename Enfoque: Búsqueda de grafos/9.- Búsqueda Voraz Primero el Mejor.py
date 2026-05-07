# DEFINICIÓN DEL GRAFO
# Cada nodo representa un punto del grafo
# y cada lista contiene los nodos vecinos conectados.
red_nodos = {
    'A': ['B', 'C'], 'B': ['A', 'D', 'E'], 'C': ['A', 'F'],
    'D': ['B', 'G', 'H'], 'E': ['B', 'I'], 'F': ['C', 'J', 'K'],
    'G': ['D', 'L'], 'H': ['D'], 'I': ['E', 'M', 'N'],
    'J': ['F'], 'K': ['F', 'O'], 'L': ['G', 'P'],
    'M': ['I'], 'N': ['I', 'Q'], 'O': ['K'],
    'P': ['L'], 'Q': ['N', 'R'], 'R': ['Q']
}

# VALORES HEURÍSTICOS
# La heurística representa una estimación
# de qué tan lejos está cada nodo de la meta 'Q'.
# Mientras menor sea el valor, más prometedor es el nodo.
valores_heuristicos = {
    'Q': 0, 'N': 1, 'R': 1, 'I': 2, 'E': 3, 'M': 3,
    'B': 4, 'A': 5, 'D': 5, 'C': 6, 'G': 6, 'H': 6,
    'F': 7, 'L': 7, 'J': 8, 'K': 8, 'P': 8, 'O': 9
}

# FUNCIÓN DE BÚSQUEDA VORAZ PRIMERO EL MEJOR
def busqueda_greedy(red, heuristica_nodos, inicio, objetivo):
    
    # Mensaje inicial indicando el nodo origen y meta
    print(f"--- Búsqueda Voraz Primero el Mejor (Origen: {inicio}, Meta: {objetivo}) ---")
    
    # Cola de prioridad manual
    # Guarda tuplas con:
    # (valor heurístico, nodo actual, ruta recorrida)
    lista_prioridad = [(heuristica_nodos[inicio], inicio, [inicio])]
    
    # Conjunto para evitar visitar nodos repetidos
    nodos_visitados = set()

    # El ciclo continúa mientras existan nodos por evaluar
    while lista_prioridad:
        
        # Ordenamos la lista según el menor valor heurístico
        # El nodo más prometedor quedará al inicio
        lista_prioridad.sort(key=lambda elemento: elemento[0])
        
        # Extraemos el nodo con mejor heurística
        heuristica_actual, nodo_actual, ruta_actual = lista_prioridad.pop(0)
        
        # Mostramos el nodo que se está evaluando
        print(f"Evaluando: {nodo_actual} (Valor f(n) = h(n) = {heuristica_actual})")

        # Verificamos si llegamos a la meta
        if nodo_actual == objetivo:
            print(f"\n¡ÉXITO! Meta '{objetivo}' encontrada.")
            print(f"Ruta Voraz: {ruta_actual}")
            return True

        # Solo procesamos nodos no visitados
        if nodo_actual not in nodos_visitados:
            
            # Marcamos el nodo como visitado
            nodos_visitados.add(nodo_actual)
            
            # Obtenemos los vecinos del nodo actual
            conexiones = red.get(nodo_actual, [])
            
            # Recorremos cada vecino
            for siguiente_nodo in conexiones:
                
                # Evitamos agregar vecinos ya visitados
                if siguiente_nodo not in nodos_visitados:
                    
                    # Obtenemos el valor heurístico del vecino
                    # Si no existe, se asigna infinito
                    heuristica_vecino = heuristica_nodos.get(
                        siguiente_nodo,
                        float('inf')
                    )
                    
                    # Agregamos el vecino a la cola de prioridad
                    # junto con la nueva ruta recorrida
                    lista_prioridad.append(
                        (
                            heuristica_vecino,
                            siguiente_nodo,
                            ruta_actual + [siguiente_nodo]
                        )
                    )

    # Si la cola queda vacía y no se encontró la meta
    print(f"\nLa meta '{objetivo}' no es alcanzable.")
    return False

# PRUEBA DEL ALGORITMO
# Se inicia la búsqueda desde el nodo 'A'
# hasta encontrar el nodo objetivo 'Q'.
busqueda_greedy(
    red_nodos,
    valores_heuristicos,
    inicio='A',
    objetivo='Q'
)