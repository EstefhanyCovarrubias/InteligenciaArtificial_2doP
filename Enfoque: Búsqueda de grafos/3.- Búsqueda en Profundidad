# Representación del grafo (estructura jerárquica tipo árbol)
estructura = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'F'],
    'D': ['G', 'H'],
    'E': ['I', 'J'],
    'F': ['K', 'L'],
    'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': []
}

def busqueda_profundidad(grafo, inicio, objetivo):
    """
    Implementación del algoritmo DFS (Depth-First Search).
    Explora una rama completa antes de retroceder a otra.
    """

    # Usamos una pila: el último nodo que entra es el primero en salir (LIFO)
    # Cada elemento guarda: (nodo_actual, camino_recorrido)
    pila = [(inicio, [inicio])]

    # Conjunto para evitar visitar nodos repetidos
    visitados = set()

    # Mientras haya nodos en la pila
    while pila:

        # Extraemos el último nodo agregado (comportamiento LIFO)
        nodo_actual, camino = pila.pop()
        print(f"Visitando nodo: {nodo_actual}")

        # Si encontramos el objetivo, terminamos
        if nodo_actual == objetivo:
            print("\n--- OBJETIVO ENCONTRADO ---")
            print(f"Nodo: {objetivo}")
            print(f"Ruta seguida: {' -> '.join(camino)}")
            return True

        # Solo exploramos si no ha sido visitado antes
        if nodo_actual not in visitados:

            # Marcamos como visitado
            visitados.add(nodo_actual)

            # Obtenemos los vecinos del nodo actual
            vecinos = grafo.get(nodo_actual, [])

            # Recorremos los vecinos en orden inverso
            # Esto se hace para que al usar la pila, se respete el orden original
            for vecino in reversed(vecinos):

                # Solo agregamos si no ha sido visitado
                if vecino not in visitados:

                    # Construimos el nuevo camino agregando el vecino
                    nuevo_camino = camino + [vecino]

                    # Apilamos el nuevo nodo junto con su ruta
                    pila.append((vecino, nuevo_camino))

    # Si se vacía la pila y no se encontró el objetivo
    print(f"\nNo se encontró el nodo '{objetivo}'.")
    return False

print("Iniciando búsqueda en profundidad...\n")
busqueda_profundidad(estructura, inicio='A', objetivo='H')