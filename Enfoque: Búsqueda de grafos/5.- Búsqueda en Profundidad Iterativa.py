# Grafo que representa conexiones entre nodos
grafo_iddfs = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'],
    'D': ['G', 'H'], 'E': ['I'], 'F': ['J', 'K'],
    'G': ['L'], 'I': ['M', 'N'], 'K': ['O'],
    'L': ['P'], 'N': ['Q'], 'Q': ['R'],
    'H': [], 'J': [], 'M': [], 'O': [], 'P': [], 'R': []
}

# --- FUNCIÓN BASE: BÚSQUEDA EN PROFUNDIDAD LIMITADA (DLS) ---
def dls_iterativo(grafo, nodo, objetivo, limite, camino=[]):
    """
    Esta función realiza una búsqueda DFS con límite de profundidad.
    Es el "motor" que IDDFS utiliza en cada iteración.
    """

    # Construimos el camino actual incluyendo el nodo visitado
    ruta_actual = camino + [nodo]

    # La profundidad depende de cuántos nodos llevamos recorridos
    profundidad = len(camino)

    # Caso 1: encontramos el objetivo
    if nodo == objetivo:
        return "ENCONTRADO", ruta_actual

    # Caso 2: alcanzamos el límite de profundidad
    if profundidad >= limite:
        # Si hay más hijos pero no podemos bajar → hubo corte
        if grafo.get(nodo, []):
            return "CORTE", None
        else:
            # Nodo sin hijos → simplemente no hay más caminos
            return "SIN_RESULTADO", None

    # Exploramos los hijos (recursividad tipo DFS)
    hijos = grafo.get(nodo, [])
    hubo_corte = False  # Para detectar si hubo nodos más profundos no explorados

    for hijo in hijos:
        estado, resultado = dls_iterativo(grafo, hijo, objetivo, limite, ruta_actual)

        # Si encontramos el objetivo, regresamos inmediatamente
        if estado == "ENCONTRADO":
            return "ENCONTRADO", resultado

        # Si hubo corte en algún hijo, lo registramos
        if estado == "CORTE":
            hubo_corte = True

    # Después de explorar todos los hijos:
    if hubo_corte:
        return "CORTE", None
    else:
        return "SIN_RESULTADO", None


# --- FUNCIÓN PRINCIPAL: IDDFS ---
def iddfs(grafo, inicio, objetivo, limite_max):
    """
    Implementación de Iterative Deepening DFS.
    Ejecuta múltiples DLS aumentando el límite en cada iteración.
    """

    print(f"Iniciando IDDFS para buscar: {objetivo}")

    # Bucle que incrementa el límite de profundidad progresivamente
    for limite in range(limite_max + 1):

        print(f"\nProbando con límite de profundidad: {limite}")

        # Ejecutamos DLS con el límite actual
        estado, camino = dls_iterativo(grafo, inicio, objetivo, limite)

        # Si encontramos el objetivo, terminamos todo el proceso
        if estado == "ENCONTRADO":
            print("\n--- OBJETIVO ENCONTRADO ---")
            print(f"Profundidad alcanzada: {limite}")
            print(f"Ruta: {' -> '.join(camino)}")
            return True

        # Si NO hubo cortes, significa que ya exploramos TODO el grafo
        # y el objetivo no existe
        if estado == "SIN_RESULTADO":
            print("\nEl objetivo no existe en el grafo.")
            return False

        # Si hubo corte, significa que aún hay niveles más profundos
        print("Aún hay niveles más profundos, aumentando límite...")

    # Si se alcanza el límite máximo sin éxito
    print(f"\nNo se encontró el objetivo hasta profundidad {limite_max}")
    return False

iddfs(grafo_iddfs, inicio='A', objetivo='M', limite_max=8)