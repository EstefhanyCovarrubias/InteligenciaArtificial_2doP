import random

# --- 1. Definimos la meta y los "genes" disponibles ---
OBJETIVO = "DESTINO"                 # Palabra que queremos alcanzar
ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Conjunto de caracteres posibles
POBLACION_INICIAL = 100              # Tamaño de la población

def crear_gen():
    """Genera una letra aleatoria del alfabeto disponible."""
    return random.choice(ALFABETO)

def crear_individuo():
    """Crea un individuo (lista de letras) con la misma longitud que la meta."""
    return [crear_gen() for _ in range(len(OBJETIVO))]

def evaluar_individuo(individuo):
    """
    Función de aptitud (fitness): cuenta cuántas letras coinciden en la posición correcta.
    Ejemplo: OBJETIVO = 'DESTINO', individuo = 'DXXTXXO' → aptitud = 3.
    """
    puntos = 0
    for i in range(len(OBJETIVO)):
        if individuo[i] == OBJETIVO[i]:
            puntos += 1
    return puntos

def reproducir(padre1, padre2):
    """Combina genes: mitad izquierda del padre1 + mitad derecha del padre2."""
    corte = random.randint(1, len(OBJETIVO) - 1)
    hijo = padre1[:corte] + padre2[corte:]
    return hijo

def mutacion(individuo, probabilidad=0.1):
    """Aplica mutaciones aleatorias para mantener diversidad genética."""
    for i in range(len(individuo)):
        if random.random() < probabilidad:
            individuo[i] = crear_gen()
    return individuo

def evolucion_genetica():
    print(f"--- Iniciando Evolución Genética (Meta: '{OBJETIVO}') ---")
    
    # Generación 0: población inicial aleatoria
    poblacion = [crear_individuo() for _ in range(POBLACION_INICIAL)]
    generacion = 1
    
    while True:
        # Evaluamos cada individuo y guardamos su aptitud
        evaluados = [(evaluar_individuo(ind), ind) for ind in poblacion]
        
        # Ordenamos por aptitud descendente (mejores primero)
        evaluados.sort(key=lambda x: x[0], reverse=True)
        
        # Seleccionamos al mejor de la generación
        mejor_puntaje, mejor_individuo = evaluados[0]
        mejor_palabra = "".join(mejor_individuo)
        
        print(f"Generación {generacion} | Mejor: {mejor_palabra} | Aptitud: {mejor_puntaje}/{len(OBJETIVO)}")
        
        # Condición de éxito: alcanzamos la meta
        if mejor_puntaje == len(OBJETIVO):
            print(f"\n¡ÉXITO! La evolución alcanzó la meta en la generación {generacion}.")
            break
            
        # --- CREACIÓN DE LA NUEVA GENERACIÓN ---
        nueva_poblacion = []
        
        # Elitismo: mantenemos los 10 mejores individuos
        elite = [ind for puntaje, ind in evaluados[:10]]
        nueva_poblacion.extend(elite)
        
        # Reproducción y mutación para completar la población
        while len(nueva_poblacion) < POBLACION_INICIAL:
            padre1 = random.choice(evaluados[:50])[1]
            padre2 = random.choice(evaluados[:50])[1]
            
            hijo = reproducir(padre1, padre2)
            hijo = mutacion(hijo)
            
            nueva_poblacion.append(hijo)
            
        # Reemplazamos la población anterior
        poblacion = nueva_poblacion
        generacion += 1

# --- PRUEBA DEL CÓDIGO ---
evolucion_genetica()
