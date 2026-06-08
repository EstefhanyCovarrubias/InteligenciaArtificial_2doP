# SIMULADOR DEL ALGORITMO DE DIJKSTRA
# ==========================================================
# Este programa encuentra la ruta más corta desde un punto de inicio hacia todos los demás puntos de un mapa.

# Imagina que quieres ir de tu casa a diferentes lugares
# de la ciudad y deseas conocer el camino que requiere
# menos distancia o menos costo.

# El algoritmo de Dijkstra analiza todas las rutas posibles
# y siempre elige primero la opción más económica disponible.
# ==========================================================

# librería heapq.
# Esta herramienta nos permite administrar una "cola de prioridad".
#
# Una cola de prioridad funciona como una fila inteligente:
# siempre coloca primero el elemento más importante.
#
# En nuestro caso, lo más importante será el nodo que tenga
# la distancia más pequeña hasta el momento.
import heapq

# DEFINICIÓN DEL GRAFO
# Un grafo es una representación de lugares conectados.
#
# Cada letra representa un lugar o nodo.
#
# Los números representan el costo o distancia para viajar
# entre dos lugares.
#
# Ejemplo:
# A -> B = 4
# significa que para ir de A a B debemos recorrer 4 unidades.
#
# Este grafo puede representar:
# - Ciudades
# - Calles
# - Computadoras conectadas
# - Estaciones de transporte
# - Cualquier sistema de rutas
# ==========================================================

grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

# FUNCIÓN DIJKSTRA

# Esta función es el corazón del programa.
#
# Recibe:
# - El grafo (mapa de conexiones)
# - El nodo de inicio
#
# Su objetivo es calcular la distancia mínima desde
# el punto inicial hacia todos los demás puntos.
# ==========================================================

def dijkstra(grafo, inicio):
    # CREACIÓN DE LA TABLA DE DISTANCIAS
    # Al comenzar, no conocemos la distancia hacia ningún
    # nodo, por lo tanto asignamos infinito.
    #
    # "Infinito" significa:
    # "Todavía no sabemos cómo llegar".
    #
    # Luego establecemos que la distancia del nodo inicial
    # hacia sí mismo es cero.
    # ------------------------------------------------------

    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    # COLA DE PRIORIDAD

    # Aquí guardaremos los nodos pendientes por analizar.
    #
    # Cada elemento se guarda así:
    #
    # (distancia, nodo)
    #
    # Ejemplo:
    # (4, 'B')
    #
    # significa:
    # "El nodo B se encuentra a una distancia de 4".
    #
    # Comenzamos agregando el nodo inicial.
    # ------------------------------------------------------

    cola_prioridad = [(0, inicio)]

    # CONJUNTO DE VISITADOS
    # ------------------------------------------------------
    #
    # Aquí almacenaremos los nodos que ya fueron analizados.
    #
    # Esto evita revisar el mismo nodo varias veces.
    # ------------------------------------------------------

    visitados = set()


    # Variable utilizada únicamente para mostrar los pasos
    # de la simulación en pantalla.
    paso = 1

    print("\n===== SIMULACIÓN DE DIJKSTRA =====\n")


    # ------------------------------------------------------
    # BUCLE PRINCIPAL
    # ------------------------------------------------------
    #
    # El algoritmo continuará ejecutándose mientras existan
    # nodos pendientes dentro de la cola de prioridad.
    # ------------------------------------------------------

    while cola_prioridad:


        # --------------------------------------------------
        # EXTRAER EL NODO MÁS IMPORTANTE
        # --------------------------------------------------
        #
        # heapq.heappop() obtiene automáticamente el nodo
        # con la distancia más pequeña.
        #
        # Esto es precisamente la idea principal del
        # algoritmo de Dijkstra.
        # --------------------------------------------------

        distancia_actual, nodo_actual = heapq.heappop(
            cola_prioridad
        )


        # --------------------------------------------------
        # VERIFICAR SI YA FUE VISITADO
        # --------------------------------------------------
        #
        # Si ya analizamos este nodo anteriormente,
        # lo ignoramos para evitar trabajo innecesario.
        # --------------------------------------------------

        if nodo_actual in visitados:
            continue


        # Marcamos el nodo como visitado.
        visitados.add(nodo_actual)


        # --------------------------------------------------
        # INFORMACIÓN DE LA SIMULACIÓN
        # --------------------------------------------------

        print(f"\nPASO {paso}")
        print(f"Nodo actual: {nodo_actual}")
        print(f"Distancia acumulada: {distancia_actual}")


        # --------------------------------------------------
        # ANALIZAR LOS VECINOS
        # --------------------------------------------------
        #
        # Ahora revisamos todos los lugares conectados
        # directamente al nodo actual.
        #
        # Ejemplo:
        # Si estamos en A, revisamos B y C.
        # --------------------------------------------------

        for vecino, peso in grafo[nodo_actual].items():

            # ----------------------------------------------
            # CALCULAR NUEVA DISTANCIA
            # ----------------------------------------------
            #
            # Sumamos:
            #
            # distancia acumulada hasta el nodo actual
            # +
            # costo para llegar al vecino
            #
            # Esto nos permite saber cuánto costaría
            # recorrer esa nueva ruta.
            # ----------------------------------------------

            nueva_distancia = distancia_actual + peso


            print(
                f"Analizando camino "
                f"{nodo_actual} -> {vecino}"
            )

            print(
                f"Costo de este tramo: {peso}"
            )


            # ----------------------------------------------
            # COMPARACIÓN DE RUTAS
            # ----------------------------------------------
            #
            # Si encontramos un camino más corto,
            # actualizamos la tabla de distancias.
            #
            # Esto significa:
            #
            # "Acabamos de descubrir una mejor ruta".
            # ----------------------------------------------

            if nueva_distancia < distancias[vecino]:

                distancias[vecino] = nueva_distancia

                # Guardamos el vecino en la cola para
                # analizarlo posteriormente.
                heapq.heappush(
                    cola_prioridad,
                    (nueva_distancia, vecino)
                )

                print(
                    f"Mejor ruta encontrada."
                )

                print(
                    f"Nueva distancia para "
                    f"{vecino}: {nueva_distancia}"
                )

            else:

                print(
                    "La ruta actual no mejora "
                    "la distancia conocida."
                )


        # --------------------------------------------------
        # MOSTRAR ESTADO ACTUAL
        # --------------------------------------------------
        #
        # Esto permite observar cómo el algoritmo
        # va encontrando rutas cada vez mejores.
        # --------------------------------------------------

        print("\nTabla temporal de distancias:")

        for nodo, distancia in distancias.items():
            print(f"{nodo}: {distancia}")

        print("\n" + "=" * 50)

        paso += 1


    # ------------------------------------------------------
    # RESULTADO FINAL
    # ------------------------------------------------------
    #
    # Cuando la cola queda vacía significa que ya fueron
    # exploradas todas las rutas posibles.
    #
    # La tabla de distancias contendrá las mejores rutas
    # encontradas desde el nodo inicial.
    # ------------------------------------------------------

    return distancias


# ==========================================================
# EJECUCIÓN DEL PROGRAMA
# ==========================================================
#
# Indicamos que el punto de partida será el nodo A.
#
# El algoritmo calculará las rutas mínimas desde A hacia
# todos los demás nodos del grafo.
# ==========================================================

resultado = dijkstra(grafo, 'A')


# ==========================================================
# MOSTRAR RESULTADOS FINALES
# ==========================================================
#
# Finalmente mostramos las distancias mínimas encontradas.
#
# Ejemplo:
# A -> F = 13
#
# Significa que la ruta más corta desde A hasta F tiene
# un costo total de 13 unidades.
# ==========================================================

print("\n===== RESULTADOS FINALES =====")

for nodo, distancia in resultado.items():
    print(
        f"Distancia mínima desde A hasta "
        f"{nodo}: {distancia}"
    )