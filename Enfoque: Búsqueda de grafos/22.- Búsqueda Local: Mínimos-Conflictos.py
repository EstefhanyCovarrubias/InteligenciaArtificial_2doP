import random

# --- Mínimos Conflictos ---
# Estrategia de búsqueda local: inicia con una asignación completa y corrige conflictos iterativamente.

# Variables: médicos
medicos = ['Dr. A', 'Dra. B', 'Dr. C']

# Dominios: turnos
turnos = ['Mañana', 'Noche']

# Restricciones: médicos que no pueden compartir turno
conflictos = {
    'Dr. A': ['Dra. B'],
    'Dra. B': ['Dr. A', 'Dr. C'],
    'Dr. C': ['Dra. B']
}

def optimizar_guardias(max_intentos=50):
    """Corrige una agenda inicial usando mínimos conflictos."""
    # Asignación inicial aleatoria
    agenda = {m: random.choice(turnos) for m in medicos}
    print(f"--- Agenda inicial: {agenda} ---")

    for i in range(max_intentos):
        # Detectar médicos en conflicto
        en_conflicto = []
        for m in medicos:
            for colega in conflictos[m]:
                if agenda[m] == agenda[colega]:
                    en_conflicto.append(m)
                    break

        # Si no hay conflictos, éxito
        if not en_conflicto:
            print(f"\n[Éxito] Agenda optimizada en {i} pasos.")
            print("Resultado:", agenda)
            return agenda

        # Elegir médico en conflicto y reasignar turno
        elegido = random.choice(en_conflicto)
        print(f"Iteración {i}: resolviendo conflicto de {elegido}")
        agenda[elegido] = min(turnos, key=lambda t: sum(
            1 for colega in conflictos[elegido] if agenda.get(colega) == t
        ))
        print("  -> Nuevo estado:", agenda)

    print("\n[Fin] Límite de intentos alcanzado. Persisten conflictos.")
    return agenda

# --- Ejecución ---
optimizar_guardias()
