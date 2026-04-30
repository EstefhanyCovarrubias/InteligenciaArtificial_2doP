# Grafo que representa conexiones entre nodos (estructura tipo árbol)
grafo_dls = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G', 'H'],
    'E': ['I'],
    'F': ['J', 'K'],
    'G': ['L'],
    'I': ['M', 'N'],
    'K': ['O'],
    'L': ['P'],
    'N': ['Q'],
    'Q': ['R'],
    'H': [], 'J': [], 'M': [], 'O': [], 'P': [], 'R': []
}

def dls(grafo, nodo, objetivo, limite, camino_actual=[]):
    """
    Implementación de Depth-Limited Search (DLS).
    Funciona como DFS, pero con un límite máximo de profundidad.
    """

    # Construimos el nuevo camino incluyendo el nodo actual
    nuevo_camino = camino_actual + [nodo]

    # La profundidad actual se calcula según cuántos nodos llevamos recorridos
    profundidad_actual = len(camino_actual)

    print(f"Visitando: {nodo} | Profundidad: {profundidad_actual} | Límite: {limite}")

    # 1. Verificamos si encontramos el objetivo
    if nodo == objetivo:
        return "ENCONTRADO", nuevo_camino

    # 2. Verificamos si alcanzamos el límite de profundidad
    # Si ya llegamos al límite, no podemos seguir bajando más
    if profundidad_actual >= limite:

        # Si el nodo tiene hijos pero no podemos explorarlos → hubo corte (cutoff)
        if grafo.get(nodo, []):
            return "CORTE", None
        else:
            # Si no tiene hijos, simplemente es un camino sin salida
            return "SIN_RESULTADO", None

    # 3. Exploramos los nodos hijos (recursividad)
    hijos = grafo.get(nodo, [])

    # Variable para saber si en algún punto se cortó la búsqueda
    hubo_corte = False

    for hijo in hijos:

        # Llamada recursiva: seguimos bajando en profundidad
        estado, resultado_camino = dls(grafo, hijo, objetivo, limite, nuevo_camino)

        # Si encontramos el objetivo, retornamos inmediatamente
        if estado == "ENCONTRADO":
            return "ENCONTRADO", resultado_camino

        # Si hubo corte en algún hijo, lo registramos
        if estado == "CORTE":
            hubo_corte = True

    # 4. Determinamos qué regresar después de explorar todos los hijos
    if hubo_corte:
        # Significa que no encontramos el objetivo, pero sí hay más niveles abajo
        return "CORTE", None
    else:
        # No hay más caminos ni niveles adicionales
        return "SIN_RESULTADO", None


def ejecutar_dls(grafo, inicio, objetivo, limite_max):
    """
    Función auxiliar que interpreta el resultado del algoritmo DLS.
    """

    print(f"\n--- INICIANDO BÚSQUEDA DLS (Objetivo: {objetivo}, Límite: {limite_max}) ---")

    estado, camino = dls(grafo, inicio, objetivo, limite_max)

    if estado == "ENCONTRADO":
        print("\nResultado: Objetivo encontrado")
        print(f"Camino: {' -> '.join(camino)}")

    elif estado == "CORTE":
        print("\nResultado: Se alcanzó el límite de profundidad")
        print("El objetivo podría estar en niveles más profundos")

    else:
        print("\nResultado: Objetivo no encontrado en el rango permitido")


# PRUEBAS

# Caso 1: Límite insuficiente
ejecutar_dls(grafo_dls, 'A', 'L', limite_max=3)

# Caso 2: Límite suficiente
ejecutar_dls(grafo_dls, 'A', 'F', limite_max=5)