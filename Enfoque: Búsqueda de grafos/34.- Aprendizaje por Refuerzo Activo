from collections import deque

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Nodo objetivo
objetivo = 'D'

# -----------------------------
# MEMORIA DE APRENDIZAJE
# -----------------------------
# Guarda "qué tan bueno es visitar un nodo"
memoria_refuerzo = {nodo: 0 for nodo in grafo}

# -----------------------------
# FUNCIÓN DE BÚSQUEDA (BFS con refuerzo)
# -----------------------------
def busqueda_reforzada(inicio):
    cola = deque([[inicio]])  # cada elemento es un camino completo
    visitados = set()
    
    historial = []  # Para ver TODO el recorrido del algoritmo
    
    while cola:
        camino = cola.popleft()
        nodo_actual = camino[-1]
        
        # Registrar paso (para ver el recorrido)
        historial.append(nodo_actual)
        
        if nodo_actual == objetivo:
            # Refuerzo positivo a todo el camino
            for n in camino:
                memoria_refuerzo[n] += 1
            return camino, historial
        
        if nodo_actual not in visitados:
            visitados.add(nodo_actual)
            
            vecinos = grafo[nodo_actual]
            
            # Ordenar vecinos según experiencia (aprendizaje activo)
            vecinos_ordenados = sorted(
                vecinos,
                key=lambda x: memoria_refuerzo[x],
                reverse=True  # prioriza los que han sido buenos antes
            )
            
            for vecino in vecinos_ordenados:
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
    
    return None, historial

# -----------------------------
# ENTRENAMIENTO (varias búsquedas)
# -----------------------------
def entrenar(iteraciones=5):
    for i in range(iteraciones):
        camino, _ = busqueda_reforzada('A')
        print(f"Iteración {i+1}, camino encontrado: {camino}")

# -----------------------------
# FUNCIÓN PARA VER EL RECORRIDO
# -----------------------------
def ver_recorrido():
    camino, historial = busqueda_reforzada('A')
    
    print("\nRecorrido paso a paso del algoritmo:")
    print(" -> ".join(historial))
    
    print("\nCamino final encontrado:")
    print(" -> ".join(camino))
    
    print("\nMemoria de refuerzo:")
    for nodo, valor in memoria_refuerzo.items():
        print(f"{nodo}: {valor}")

entrenar(5)
ver_recorrido()