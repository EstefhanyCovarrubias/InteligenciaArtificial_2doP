# --- Backjumping ---
# Optimiza el Backtracking: salta atrás al origen real del conflicto.

# Variables: satélites
satelites = ['Sat-A', 'Sat-B', 'Sat-C']

# Dominios: canales de frecuencia
canales = ['Frecuencia-1', 'Frecuencia-2']

# Restricciones: satélites cercanos no pueden compartir canal
interferencias = {
    'Sat-A': ['Sat-B'],
    'Sat-B': ['Sat-A', 'Sat-C'],
    'Sat-C': ['Sat-B']
}

def validar(sat, canal, red):
    """Comprueba si el canal genera interferencia con vecinos ya asignados."""
    for vecino in interferencias.get(sat, []):
        if vecino in red and red[vecino] == canal:
            return False
    return True

# --- Motor de Backjumping ---
def coordinar(config=None):
    """Asigna frecuencias; retrocede al origen del conflicto si falla."""
    if config is None:
        config = {}

    # Éxito: todos los satélites configurados
    if len(config) == len(satelites):
        print("\n[Éxito] Configuración completa:", config)
        return config

    # Seleccionamos siguiente satélite
    sat = satelites[len(config)]

    for canal in canales:
        print(f"Probando {canal} en {sat}...")
        if validar(sat, canal, config):
            config[sat] = canal
            resultado = coordinar(config)
            if resultado:
                return resultado
            # Retroceso inteligente
            print(f"  [!] Conflicto. Saltando atrás desde {sat}...")
            del config[sat]

    return None

# --- Inicio ---
print("--- Sistema de Salto Atrás ---")
coordinar()
