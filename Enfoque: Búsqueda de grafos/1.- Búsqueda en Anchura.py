# Definimos el grafo usando un diccionario
# Cada clave es un nodo y su valor es una lista de nodos conectados (adyacentes)
grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E', 'F'],
    'D': ['G', 'H'],
    'E': ['I', 'J'],
    'F': ['K', 'L'],
    'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': []
}

from collections import deque  # Estructura eficiente para colas (FIFO)

def buscar_en_anchura(grafo, inicio, meta):
    """
    Esta función recorre un grafo utilizando el algoritmo BFS (Breadth-First Search).
    Su objetivo es encontrar un nodo específico explorando por niveles.
    """

    # Creamos una cola (FIFO: First In, First Out)
    # Aquí se irán guardando los nodos pendientes por explorar
    cola = deque()

    # Conjunto para registrar los nodos que ya fueron visitados
    # Esto evita procesar el mismo nodo más de una vez (muy importante en grafos)
    visitados = set()

    # Insertamos el nodo inicial en la cola para comenzar la búsqueda
    cola.append(inicio)

    # El ciclo continúa mientras haya nodos pendientes en la cola
    while cola:

        # Extraemos el nodo más antiguo (el primero que entró)
        # Esto garantiza que exploremos por niveles
        nodo_actual = cola.popleft()
        print(f"Explorando nodo: {nodo_actual}")

        # Verificamos si el nodo actual es el objetivo
        if nodo_actual == meta:
            print(f"\nObjetivo encontrado: '{meta}'")
            return True

        # Solo expandimos el nodo si no ha sido visitado antes
        if nodo_actual not in visitados:

            # Marcamos el nodo como visitado
            visitados.add(nodo_actual)

            # Obtenemos todos los vecinos del nodo actual
            # Si no tiene vecinos, se obtiene una lista vacía
            vecinos = grafo.get(nodo_actual, [])

            # Agregamos cada vecino al final de la cola
            # Esto permite que se procesen después, respetando el orden por niveles
            for vecino in vecinos:
                cola.append(vecino)

    # Si la cola se vacía y no encontramos el objetivo, significa que no existe
    print(f"\nEl nodo '{meta}' no se encontró en el grafo.")
    return False

print("Iniciando búsqueda BFS...\n")
buscar_en_anchura(grafo, inicio='A', meta='J')