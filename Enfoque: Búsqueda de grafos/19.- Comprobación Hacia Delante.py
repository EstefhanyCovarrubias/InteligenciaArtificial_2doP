# --- Forward Checking ---
# Técnica para CSP que mejora el Backtracking.
# Filtra dominios futuros y detecta fallos antes de avanzar.

# Variables: turnos
turnos = ['Mañana', 'Tarde', 'Noche']

# Dominios: equipos disponibles
personal = ['Equipo-Alfa', 'Equipo-Beta']

# Restricciones: turnos que no pueden compartir el mismo equipo
conflictos = {
    'Mañana': ['Tarde'],
    'Tarde': ['Mañana', 'Noche'],
    'Noche': ['Tarde']
}

def gestion_preventiva(asignacion=None, opciones=None):
    """Asigna equipos a turnos usando Forward Checking."""
    if asignacion is None:
        asignacion = {}
    if opciones is None:
        opciones = {t: list(personal) for t in turnos}

    # Éxito: todos los turnos cubiertos
    if len(asignacion) == len(turnos):
        print("\n[Plan exitoso]:", asignacion)
        return asignacion

    # Seleccionamos siguiente turno
    turno = turnos[len(asignacion)]

    # Probamos equipos disponibles
    for equipo in opciones[turno]:
        print(f"Evaluando {equipo} en {turno}...")
        futuro = {t: list(opciones[t]) for t in opciones}
        asignacion[turno] = equipo
        fallo = False

        # Forward Checking: reducimos opciones de vecinos
        for vecino in conflictos[turno]:
            if equipo in futuro[vecino]:
                futuro[vecino].remove(equipo)
                print(f"  -> {vecino} ahora: {futuro[vecino]}")
                if not futuro[vecino]:
                    print(f"  [!] {vecino} sin opciones. Retroceso.")
                    fallo = True

        # Si no hay fallo, seguimos recursivamente
        if not fallo:
            resultado = gestion_preventiva(asignacion, futuro)
            if resultado:
                return resultado

        # Retroceso si falla
        del asignacion[turno]

    return None

# --- Inicio ---
print("--- Asignación con Forward Checking ---")
gestion_preventiva()
