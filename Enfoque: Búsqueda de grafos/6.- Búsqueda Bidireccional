# Grafo no dirigido: cada nodo tiene conexiones en ambos sentidos
grafo_bidireccional = {
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

def busqueda_bidireccional(grafo, inicio, objetivo):
    """
    Implementación de búsqueda bidireccional.
    Se ejecutan dos BFS al mismo tiempo: uno desde el inicio y otro desde el objetivo.
    """

    # Cola para la búsqueda desde el inicio (como BFS)
    cola_inicio = [inicio]

    # Cola para la búsqueda desde el objetivo
    cola_objetivo = [objetivo]

    # Diccionarios para reconstruir el camino
    # Guardan de dónde viene cada nodo
    padres_inicio = {inicio: None}
    padres_objetivo = {objetivo: None}

    print(f"Iniciando búsqueda entre {inicio} y {objetivo}\n")

    # El algoritmo continúa mientras ambas colas tengan elementos
    while cola_inicio and cola_objetivo:

        # -------- EXPANSIÓN DESDE EL INICIO --------
        actual_inicio = cola_inicio.pop(0)
        print(f"[Desde inicio] Visitando: {actual_inicio}")

        # Si el nodo ya fue visitado por la búsqueda del objetivo → se encontraron
        if actual_inicio in padres_objetivo:
            print(f"\nIntersección encontrada en: {actual_inicio}")
            return reconstruir_camino(actual_inicio, padres_inicio, padres_objetivo)

        # Expandimos vecinos
        for vecino in grafo.get(actual_inicio, []):
            if vecino not in padres_inicio:
                padres_inicio[vecino] = actual_inicio
                cola_inicio.append(vecino)

        # -------- EXPANSIÓN DESDE EL OBJETIVO --------
        actual_objetivo = cola_objetivo.pop(0)
        print(f"[Desde objetivo] Visitando: {actual_objetivo}")

        # Si el nodo ya fue visitado por la búsqueda del inicio → se encontraron
        if actual_objetivo in padres_inicio:
            print(f"\nIntersección encontrada en: {actual_objetivo}")
            return reconstruir_camino(actual_objetivo, padres_inicio, padres_objetivo)

        # Expandimos vecinos
        for vecino in grafo.get(actual_objetivo, []):
            if vecino not in padres_objetivo:
                padres_objetivo[vecino] = actual_objetivo
                cola_objetivo.append(vecino)

    # Si alguna cola se vacía, no hay conexión
    print("\nNo existe un camino entre los nodos.")
    return False


def reconstruir_camino(punto_encuentro, padres_inicio, padres_objetivo):
    """
    Une los caminos desde el inicio y desde el objetivo
    usando el punto donde ambas búsquedas se encontraron.
    """

    # Parte 1: desde el inicio hasta el punto de encuentro
    camino_inicio = []
    nodo = punto_encuentro
    while nodo is not None:
        camino_inicio.append(nodo)
        nodo = padres_inicio[nodo]
    camino_inicio.reverse()  # Lo invertimos para que quede en orden correcto

    # Parte 2: desde el punto de encuentro hasta el objetivo
    camino_objetivo = []
    nodo = padres_objetivo[punto_encuentro]  # Evitamos duplicar el punto central
    while nodo is not None:
        camino_objetivo.append(nodo)
        nodo = padres_objetivo[nodo]

    # Unimos ambos caminos
    camino_final = camino_inicio + camino_objetivo

    print(f"\nCamino encontrado: {' -> '.join(camino_final)}")
    return camino_final

busqueda_bidireccional(grafo_bidireccional, inicio='A', objetivo='L')