# ==========================================================
# SIMULADOR DEL ALGORITMO DE PRIM
# ==========================================================
# Este programa encuentra el Árbol Parcial Mínimo (MST)
# de un grafo.
#
# El objetivo es conectar todos los nodos utilizando el
# menor costo total posible.
#
# Imagina que queremos conectar varias ciudades mediante
# carreteras, cables eléctricos o fibra óptica.
#
# Prim selecciona siempre la conexión más barata disponible
# que permita incorporar un nuevo nodo a la red.
# ==========================================================

import heapq


# ----------------------------------------------------------
# GRAFO DE EJEMPLO
# ----------------------------------------------------------
# Cada nodo representa un punto de la red.
#
# Los números representan el costo de conectar dos nodos.
# ----------------------------------------------------------

grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}


def prim(grafo, inicio):

    # Conjunto de nodos ya conectados al árbol.
    visitados = set([inicio])

    # Lista donde guardaremos las conexiones elegidas.
    arbol_minimo = []

    # Costo total acumulado.
    costo_total = 0

    # Cola de prioridad.
    # Guardará las conexiones disponibles ordenadas por costo.
    cola = []

    print("\n===== SIMULACIÓN DEL ALGORITMO DE PRIM =====\n")
    print(f"Comenzamos desde el nodo {inicio}\n")

    # Agregamos todas las conexiones iniciales.
    for vecino, peso in grafo[inicio].items():
        heapq.heappush(cola, (peso, inicio, vecino))

    paso = 1

    while cola:

        print(f"\nPASO {paso}")
        print("-" * 40)

        # Extraemos la conexión más barata disponible.
        peso, origen, destino = heapq.heappop(cola)

        print(
            f"Se analiza la conexión "
            f"{origen} -> {destino} "
            f"con costo {peso}"
        )

        # Si el destino ya pertenece al árbol,
        # la conexión se descarta.
        if destino in visitados:

            print(
                f"{destino} ya está conectado."
            )
            print("La conexión se descarta.")

            paso += 1
            continue

        # Agregamos el nuevo nodo.
        visitados.add(destino)

        # Guardamos la conexión seleccionada.
        arbol_minimo.append((origen, destino, peso))

        # Actualizamos el costo total.
        costo_total += peso

        print(
            f"Conexión aceptada: "
            f"{origen} -> {destino}"
        )

        print(
            f"Costo acumulado: "
            f"{costo_total}"
        )

        print(
            f"Nodos conectados: "
            f"{visitados}"
        )

        # Agregamos nuevas conexiones posibles.
        for vecino, nuevo_peso in grafo[destino].items():

            if vecino not in visitados:

                heapq.heappush(
                    cola,
                    (nuevo_peso, destino, vecino)
                )

                print(
                    f"Se agrega opción "
                    f"{destino} -> {vecino}"
                    f" (costo {nuevo_peso})"
                )

        paso += 1

    return arbol_minimo, costo_total


# ----------------------------------------------------------
# EJECUCIÓN DEL ALGORITMO
# ----------------------------------------------------------

arbol, costo = prim(grafo, 'A')


# ----------------------------------------------------------
# RESULTADOS FINALES
# ----------------------------------------------------------

print("\n")
print("=" * 50)
print("ÁRBOL PARCIAL MÍNIMO ENCONTRADO")
print("=" * 50)

for origen, destino, peso in arbol:
    print(
        f"{origen} -> {destino} "
        f"(Costo: {peso})"
    )

print("\nCosto total del árbol:", costo)