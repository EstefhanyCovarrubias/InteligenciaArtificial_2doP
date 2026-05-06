# Grafo con pesos: cada nodo apunta a una lista de tuplas (vecino, costo)
rutas = {
    'A': [('B', 5), ('C', 1)],
    'B': [('D', 2)],
    'C': [('E', 8), ('F', 3)],
    'D': [('G', 1), ('H', 4)],
    'E': [('I', 2), ('J', 1)],
    'F': [('K', 6), ('L', 2)],
    'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': []
}

def ucs_busqueda(grafo, origen, objetivo):
    """
    Implementación del algoritmo UCS (Uniform Cost Search).
    Su propósito es encontrar el camino con el menor costo acumulado.
    """

    # Lista que funcionará como "cola de prioridad"
    # Cada elemento tiene la forma: (costo_total, nodo_actual, camino_recorrido)
    frontera = [(0, origen, [origen])]

    # Conjunto para marcar nodos que ya fueron procesados
    visitados = set()

    # El algoritmo continúa mientras haya caminos por analizar
    while frontera:

        # Ordenamos la lista según el costo acumulado (de menor a mayor)
        # Esto asegura que siempre expandimos primero el camino más barato
        frontera.sort(key=lambda x: x[0])

        # Extraemos el elemento con menor costo
        costo_actual, nodo_actual, camino = frontera.pop(0)

        print(f"Analizando nodo: {nodo_actual} | Costo acumulado: {costo_actual}")

        # Si llegamos al objetivo, terminamos la búsqueda
        if nodo_actual == objetivo:
            print("\n--- CAMINO ENCONTRADO ---")
            print(f"Destino: {objetivo}")
            print(f"Ruta: {' -> '.join(camino)}")
            print(f"Costo total: {costo_actual}")
            return True

        # Solo expandimos el nodo si no ha sido visitado antes
        if nodo_actual not in visitados:

            # Marcamos como visitado para no repetir procesos
            visitados.add(nodo_actual)

            # Obtenemos los vecinos y sus costos asociados
            vecinos = grafo.get(nodo_actual, [])

            # Recorremos cada posible camino desde el nodo actual
            for vecino, costo in vecinos:

                # Evitamos agregar nodos ya procesados
                if vecino not in visitados:

                    # Calculamos el nuevo costo acumulado sumando el costo del tramo
                    nuevo_costo = costo_actual + costo

                    # Generamos el nuevo camino agregando el vecino
                    nuevo_camino = camino + [vecino]

                    # Insertamos esta nueva opción en la frontera
                    frontera.append((nuevo_costo, vecino, nuevo_camino))

    # Si se vacía la frontera sin encontrar el objetivo
    print(f"\nNo se encontró una ruta hacia '{objetivo}'.")
    return False

print("Ejecutando búsqueda de costo uniforme...\n")
ucs_busqueda(rutas, origen='A', objetivo='L')