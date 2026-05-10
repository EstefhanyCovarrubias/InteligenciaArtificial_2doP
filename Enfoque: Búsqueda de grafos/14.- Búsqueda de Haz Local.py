# --- Grafo con una "trampa" en el nodo 'X' (Máximo Local) ---
mapa_rutas = {
    'Origen': ['N1', 'N2'],
    'N1': ['Origen', 'N3', 'X'],
    'N2': ['Origen', 'N4', 'N6'], 
    'N3': ['N1'],
    'X': ['N1', 'N5'],      
    'N5': ['X', 'N6'],
    'N6': ['N5', 'N2'],      
    'N4': ['N2', 'Meta'],
    'Meta': []               # Nodo objetivo
}

# --- Heurística (valores estimados de distancia hacia la meta) ---
valores_estimados = {
    'Origen': 10, 'N1': 7, 'N2': 9, 'N3': 8, 
    'X': 4, 'N5': 5, 'N6': 6, 'N4': 3, 'Meta': 0
}

# --- Algoritmo de Búsqueda de Haz Local ---
def algoritmo_haz_local(grafo, heuristica, exploradores_iniciales, objetivo, k=2):
    print(f"--- Algoritmo de Haz Local (k={k} exploradores) ---")
    print(f"Meta a alcanzar: '{objetivo}'\n")
    
    # Lista de posiciones actuales de los exploradores
    grupo = exploradores_iniciales.copy()
    
    iteracion = 1
    while True:
        print(f"[Iteración {iteracion}] Exploradores en: {grupo}")
        
        # 1. Verificar si algún explorador ya llegó a la meta
        if objetivo in grupo:
            print(f"\n¡ÉXITO! Un explorador encontró la meta '{objetivo}'.")
            return True
            
        # 2. Recolectar todos los vecinos de todos los exploradores
        candidatos = []
        for nodo in grupo:
            vecinos = grafo.get(nodo, [])
            for vecino in vecinos:
                valor_h = heuristica.get(vecino, float('inf'))
                # Guardamos tupla: (heurística, vecino, origen)
                candidatos.append((valor_h, vecino, nodo))
                
        if not candidatos:
            print("No hay más caminos disponibles. Búsqueda detenida.")
            return False
            
        # 3. Eliminar duplicados (si varios exploradores ven el mismo nodo)
        unicos = {}
        for valor, vecino, origen in candidatos:
            if vecino not in unicos:
                unicos[vecino] = (valor, origen)
                
        # Convertimos a lista para ordenar
        lista_filtrada = [(valor, vecino, origen) for vecino, (valor, origen) in unicos.items()]
        
        # 4. Ordenar candidatos por mejor heurística (menor valor)
        lista_filtrada.sort(key=lambda x: x[0])
        
        print("  -> Opciones encontradas (ordenadas de mejor a peor):")
        for valor, vecino, origen in lista_filtrada:
            print(f"     * '{vecino}' (h={valor}) descubierto desde '{origen}'")
            
        # 5. Seleccionar los 'k' mejores candidatos
        mejores = lista_filtrada[:k]
        
        # Actualizar posiciones de exploradores
        nuevo_grupo = [vecino for valor, vecino, origen in mejores]
        
        # Verificar estancamiento (si no cambian las posiciones)
        if set(nuevo_grupo) == set(grupo):
            print("\n¡ALTO! Los exploradores quedaron atrapados en un Máximo Local.")
            return False
            
        grupo = nuevo_grupo
        print("-" * 50)
        iteracion += 1

# --- PRUEBA DEL CÓDIGO ---
exploradores_iniciales = ['N1', 'N3']
algoritmo_haz_local(mapa_rutas, valores_estimados, exploradores_iniciales, objetivo='Meta', k=2)
