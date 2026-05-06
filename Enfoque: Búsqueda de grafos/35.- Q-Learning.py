import random

# Cada nodo es un estado y cada conexión es una acción posible
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Estado objetivo (meta del agente)
objetivo = 'D'

# ----------------------------------
# FUNCIÓN DE RECOMPENSA
# Define el refuerzo que recibe el agente
# ----------------------------------
def recompensa(estado):
    if estado == objetivo:
        return 10   # recompensa alta si llega al objetivo
    else:
        return -1   # penalización por cada paso (para evitar caminos largos)

# Guarda el conocimiento, qué tan buena es cada acción en cada estado
# Q[estado][accion] = valor
# ----------------------------------
Q = {}
for estado in grafo:
    Q[estado] = {}
    for accion in grafo[estado]:
        Q[estado][accion] = 0  # inicialización en 0 (no sabe nada aún)

# ----------------------------------
# PARÁMETROS DE APRENDIZAJE
# ----------------------------------
alpha = 0.1   # tasa de aprendizaje (qué tan rápido aprende)
gamma = 0.9   # importancia del futuro (recompensas futuras)
epsilon = 0.3 # probabilidad de explorar (aprendizaje activo)

# ----------------------------------
# FUNCIÓN: elegir acción (ε-greedy)
# ----------------------------------
def elegir_accion(estado):
    # Si no hay acciones disponibles, termina
    if not grafo[estado]:
        return None
    
    # Exploración: prueba caminos nuevos (búsqueda en el grafo)
    if random.random() < epsilon:
        return random.choice(grafo[estado])
    else:
        # Explotación: usa lo aprendido (elige la mejor acción según Q)
        return max(Q[estado], key=Q[estado].get)

# ----------------------------------
# ENTRENAMIENTO (AQUÍ OCURRE EL Q-LEARNING)
# ----------------------------------
def entrenar(episodios=200):
    for _ in range(episodios):
        estado = 'A'  # estado inicial
        
        # Recorrer el grafo hasta llegar al objetivo
        while estado != objetivo:
            
            # 1. Elegir acción (explorar o explotar)
            accion = elegir_accion(estado)
            if accion is None:
                break
            
            # 2. Moverse al siguiente estado
            siguiente_estado = accion
            
            # 3. Obtener recompensa del nuevo estado
            r = recompensa(siguiente_estado)
            
            # 4. Obtener el mejor valor futuro desde el siguiente estado
            # (esto permite evaluar consecuencias a largo plazo)
            if Q[siguiente_estado]:
                max_q = max(Q[siguiente_estado].values())
            else:
                max_q = 0
            
            # Se actualiza el valor Q usando:
            # Q(s,a) = Q(s,a) + α [ r + γ * max(Q(s',a')) - Q(s,a) ]
            # - Compara lo que esperaba (Q actual)
            # - Con lo que obtuvo (recompensa + futuro esperado)
            # - Ajusta su conocimiento
            
            Q[estado][accion] = Q[estado][accion] + alpha * (
                r + gamma * max_q - Q[estado][accion]
            )
            
            # 5. Avanza al siguiente estado
            estado = siguiente_estado

# ----------------------------------
# FUNCIÓN: OBTENER EL MEJOR CAMINO APRENDIDO
# ----------------------------------
def ver_recorrido(inicio='A'):
    estado = inicio
    camino = [estado]
    
    while estado != objetivo:
        if not Q[estado]:
            break
        
        # Elegir siempre la mejor acción aprendida
        accion = max(Q[estado], key=Q[estado].get)
        estado = accion
        camino.append(estado)
        
        # Evitar ciclos infinitos
        if len(camino) > 10:
            break
    
    return camino

# ----------------------------------
# FUNCIÓN: VER CÓMO EXPLORA EL AGENTE
# (sirve para comprobar el algoritmo paso a paso)
# ----------------------------------
def debug_recorrido():
    estado = 'A'
    print("\nRecorrido paso a paso:")
    
    while estado != objetivo:
        accion = elegir_accion(estado)
        print(f"{estado} -> {accion}")
        
        if accion is None:
            break
        
        estado = accion
        
entrenar(300)

# Mostrar lo aprendido
print("Tabla Q aprendida:")
for estado in Q:
    print(estado, Q[estado])

# Mostrar mejor camino
camino = ver_recorrido()
print("\nMejor camino aprendido:")
print(" -> ".join(camino))

# Mostrar exploración
debug_recorrido()