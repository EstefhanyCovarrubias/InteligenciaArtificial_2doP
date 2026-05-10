# Algoritmo de búsqueda A* en Python
# Este programa encuentra el camino más corto entre dos nodos en un grafo

# Diccionario que representa el grafo con sus conexiones y costos
red_nodos = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Estimaciones heurísticas de distancia desde cada nodo hasta el destino
estimacion = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

# Función principal del algoritmo A*
def busqueda_astar(inicio, destino):
    # Conjunto de nodos por explorar
    abiertos = {inicio}
    # Conjunto de nodos ya explorados
    cerrados = set()
    
    # Diccionario para guardar el costo acumulado desde el inicio
    costo_acumulado = {inicio: 0}
    # Diccionario para guardar el camino recorrido
    padres = {inicio: None}
    
    while abiertos:
        # Selecciona el nodo con menor costo estimado total (g + h)
        nodo_actual = min(
            abiertos,
            key=lambda nodo: costo_acumulado[nodo] + estimacion[nodo]
        )
        
        # Si llegamos al destino, reconstruimos el camino
        if nodo_actual == destino:
            ruta = []
            while nodo_actual is not None:
                ruta.append(nodo_actual)
                nodo_actual = padres[nodo_actual]
            ruta.reverse()
            return ruta
        
        # Mueve el nodo actual de abiertos a cerrados
        abiertos.remove(nodo_actual)
        cerrados.add(nodo_actual)
        
        # Explora los vecinos del nodo actual
        for vecino, costo in red_nodos[nodo_actual].items():
            if vecino in cerrados:
                continue
            
            nuevo_costo = costo_acumulado[nodo_actual] + costo
            
            if vecino not in abiertos or nuevo_costo < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_costo
                padres[vecino] = nodo_actual
                abiertos.add(vecino)
    
    # Si no se encuentra ruta
    return None

# Ejemplo de uso del algoritmo
camino = busqueda_astar('A', 'D')
print("Camino más corto:", camino)
