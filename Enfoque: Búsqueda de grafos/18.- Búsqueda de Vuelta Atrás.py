# --- Backtracking ---
# Estrategia de búsqueda que prueba opciones paso a paso.
# Si una decisión falla, retrocede y prueba otra alternativa.

# Variables: invitados
invitados = ['Duque A', 'Conde B', 'Barón C']

# Dominios: menús disponibles
opciones_menu = ['Pescado', 'Carne']

# Restricciones: rivalidades (no pueden compartir menú si están cerca)
rivalidades = {
    'Duque A': ['Conde B'],
    'Conde B': ['Duque A', 'Barón C'],
    'Barón C': ['Conde B']
}

def protocolo_seguro(persona, plato, mesa_actual):
    """Comprueba si asignar plato genera conflicto con rivales."""
    enemigos = rivalidades.get(persona, [])
    for rival in enemigos:
        if rival in mesa_actual and mesa_actual[rival] == plato:
            return False
    return True

# --- Motor de Backtracking ---
def organizar_banquete(mesa=None):
    """Asigna platos recursivamente; retrocede si hay conflicto."""
    if mesa is None:
        mesa = {}

    # Éxito: todos los invitados tienen plato
    if len(mesa) == len(invitados):
        print("\n[Finalizado] Configuración exitosa:", mesa)
        return mesa

    # Seleccionamos siguiente invitado
    sujeto = invitados[len(mesa)]

    for plato in opciones_menu:
        print(f"Probando {plato} para {sujeto}...")
        if protocolo_seguro(sujeto, plato, mesa):
            mesa[sujeto] = plato
            resultado = organizar_banquete(mesa)
            if resultado:
                return resultado
            # Retroceso si falla
            print(f"  [!] Retrocediendo: {sujeto} no puede comer {plato}")
            del mesa[sujeto]

    return None

# --- Inicio ---
organizar_banquete()
