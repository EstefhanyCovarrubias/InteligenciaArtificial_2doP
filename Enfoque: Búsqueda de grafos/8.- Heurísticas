# Grafo que representa conexiones entre nodos (calles/intersecciones)
grafo_voraz = {
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

# Heurística: estimación de qué tan lejos está cada nodo del objetivo
# Mientras más pequeño el valor, más "cerca" creemos que está del destino
heuristica = {
    'Q': 0,
    'N': 1, 'R': 1,
    'I': 2,
    'E': 3, 'M': 3,
    'B': 4,
    'A': 5, 'D': 5,
    'C': 6, 'G': 6, 'H': 6,
    'F': 7, 'L': 7,
    'J': 8, 'K': 8, 'P': 8,
    'O': 9
}

def busqueda_voraz(grafo, h, inicio, objetivo):
    """
    Implementación de búsqueda voraz (Greedy Search).
    En cada paso elige el nodo que parece más cercano al objetivo según h(n).
    """

    print(f"Iniciando búsqueda voraz desde {inicio} hasta {objetivo}\n")

    # Lista tipo cola de prioridad: (valor_heuristico, nodo, camino)
    frontera = [(h[inicio], inicio, [inicio])]

    # Conjunto para evitar repetir nodos (evitar ciclos)
    visitados = set()

    while frontera:

        # Ordenamos para elegir el nodo con menor heurística
        # (el que "parece" más cercano al objetivo)
        frontera.sort(key=lambda x: x[0])

        valor_h, nodo_actual, camino = frontera.pop(0)

        print(f"Evaluando: {nodo_actual} | h(n) = {valor_h}")

        # Si llegamos al objetivo, terminamos
        if nodo_actual == objetivo:
            print("\n--- OBJETIVO ALCANZADO ---")
            print(f"Ruta: {' -> '.join(camino)}")
            return True

        # Solo exploramos si no ha sido visitado antes
        if nodo_actual not in visitados:

            visitados.add(nodo_actual)

            # Revisamos los vecinos del nodo actual
            vecinos = grafo.get(nodo_actual, [])

            for vecino in vecinos:

                if vecino not in visitados:

                    # Obtenemos la heurística del vecino
                    # Si no existe, asumimos que está muy lejos (infinito)
                    valor_vecino = h.get(vecino, float('inf'))

                    # Agregamos a la frontera con su nuevo camino
                    frontera.append((valor_vecino, vecino, camino + [vecino]))

    # Si no se encuentra el objetivo
    print("\nNo se encontró una ruta al objetivo")
    return False


busqueda_voraz(grafo_voraz, heuristica, inicio='A', objetivo='K')