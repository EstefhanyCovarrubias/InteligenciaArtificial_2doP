import copy

# --- Cutset Conditioning ---
# Si fijamos un nodo, el grafo con ciclos se convierte en un árbol y se resuelve más fácil.

# Variables: modos de frecuencia
modos = ['Frecuencia-A', 'Frecuencia-B', 'Frecuencia-C']

# Grafo con ciclo: 1-2-3-4-1
red = {
    'Nodo_1': ['Nodo_2', 'Nodo_4'],
    'Nodo_2': ['Nodo_1', 'Nodo_3'],
    'Nodo_3': ['Nodo_2', 'Nodo_4'],
    'Nodo_4': ['Nodo_3', 'Nodo_1']
}

# Nodo de corte y secuencia lineal
corte = 'Nodo_1'
cadena = ['Nodo_2', 'Nodo_3', 'Nodo_4']

def configurar_linea(indice, secuencia, config, opciones):
    """Configura nodos restantes como cadena lineal."""
    if indice >= len(secuencia):
        return True

    actual = secuencia[indice]
    for f in opciones[actual]:
        # Verificar interferencia con vecinos
        if any(config.get(v) == f for v in red[actual]):
            continue
        config[actual] = f
        print(f"      {actual} -> {f}")
        if configurar_linea(indice + 1, secuencia, config, opciones):
            return True
        del config[actual]
    return False

def estabilizar():
    """Rompe ciclo fijando un nodo y resuelve el resto como árbol."""
    print("--- Estabilización por Corte ---")
    print(f"[*] Nodo de corte: {corte}")

    base = {n: modos.copy() for n in red.keys()}

    for f in modos:
        print(f"\nAnclando {corte} en {f}...")
        config = {corte: f}
        opciones = copy.deepcopy(base)
        error = False

        # Restringir vecinos del nodo de corte
        for v in red[corte]:
            if f in opciones[v]:
                opciones[v].remove(f)
                print(f"  -> {v} bloquea {f}")
                if not opciones[v]:
                    error = True
        if error:
            print("  [X] Configuración inválida. Reintentando...")
            continue

        # Resolver cadena lineal
        print(f"  [*] Ciclo abierto. Configurando {cadena}")
        if configurar_linea(0, cadena, config, opciones):
            print("\n[Éxito] Red estabilizada.")
            return config

    print("\n[!] No se encontró configuración estable.")
    return None

# --- Ejecución ---
resultado = estabilizar()
if resultado:
    print("\nEstado final:")
    for nodo, f in resultado.items():
        print(f"  {nodo} >> {f}")
