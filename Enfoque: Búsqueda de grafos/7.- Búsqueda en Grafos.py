# Grafo con ciclos (conexiones en ambos sentidos)
grafo_social = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J', 'K'],
    'G': ['D', 'L'],
    'H': ['D'],
    'I': ['E', 'M', 'N'],
    'J': ['F'],
    'K': ['F', 'O'],
    'L': ['G', 'P'],
    'M': ['I'],
    'N': ['I', 'Q'],
    'O': ['K'],
    'P': ['L'],
    'Q': ['N', 'R'],
    'R': ['Q']
}

def busqueda_en_grafo(grafo, inicio, objetivo):
    """
    Implementación de búsqueda en grafos (tipo BFS con control de visitados).
    La clave es evitar ciclos usando un conjunto de nodos visitados.
    """

    print(f"Buscando conexión entre {inicio} y {objetivo}\n")

    # Cola de exploración (FIFO): guarda (nodo_actual, camino_recorrido)
    cola = [(inicio, [inicio])]

    # Conjunto que almacena nodos ya visitados
    # Esto evita ciclos infinitos (ejemplo: A -> B -> A -> B...)
    visitados = set()

    # Mientras haya nodos pendientes por explorar
    while cola:

        # Extraemos el primer elemento de la cola (FIFO)
        nodo_actual, camino = cola.pop(0)

        # Si encontramos el objetivo, terminamos
        if nodo_actual == objetivo:
            print("¡Objetivo encontrado!")
            print(f"Camino: {' -> '.join(camino)}")
            print(f"Número de pasos: {len(camino) - 1}")
            return True

        # Solo procesamos el nodo si no ha sido visitado antes
        if nodo_actual not in visitados:

            # Marcamos el nodo como visitado
            visitados.add(nodo_actual)
            print(f"Visitando: {nodo_actual}")

            # Obtenemos vecinos del nodo actual
            vecinos = grafo.get(nodo_actual, [])

            for vecino in vecinos:

                # Si ya fue visitado, lo ignoramos para evitar ciclos
                if vecino in visitados:
                    print(f"  - {vecino} ya fue visitado, se omite")
                else:
                    # Si no ha sido visitado, lo agregamos a la cola
                    print(f"  - {vecino} agregado a la cola")
                    nuevo_camino = camino + [vecino]
                    cola.append((vecino, nuevo_camino))

    # Si se vacía la cola sin encontrar el objetivo
    print(f"\nNo existe camino hacia {objetivo}")
    return False

busqueda_en_grafo(grafo_social, inicio='A', objetivo='K')