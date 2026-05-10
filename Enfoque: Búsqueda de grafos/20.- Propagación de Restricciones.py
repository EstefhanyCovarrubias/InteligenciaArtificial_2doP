# --- AC-3 (Arc Consistency) ---
# Preprocesa dominios en CSP para eliminar valores inválidos.
# Propaga restricciones entre variables conectadas hasta estabilizar.

# Variables: terminales
terminales = ['Norte (A)', 'Central (B)', 'Sur (C)']

# Dominios: protocolos disponibles
protocolos = ['Escaneo-Bio', 'Escaneo-RayosX']

# Restricciones: conexiones que requieren protocolos distintos
conexiones = {
    'Norte (A)': ['Central (B)'],
    'Central (B)': ['Norte (A)', 'Sur (C)'],
    'Sur (C)': ['Central (B)']
}

def ac3_seguridad():
    """Aplica AC-3 para depurar dominios de protocolos."""
    dominios = {t: list(protocolos) for t in terminales}
    print("--- Depuración AC-3 ---")
    print("Dominios iniciales:", dominios, "\n")

    cambios = True
    while cambios:
        cambios = False
        for t in terminales:
            for vecino in conexiones[t]:
                for p in dominios[t][:]:
                    # Si todos los valores del vecino son iguales al actual, lo eliminamos
                    if all(p == pv for pv in dominios[vecino]):
                        dominios[t].remove(p)
                        cambios = True
                        print(f"  [!] Eliminado {p} de {t} por conflicto con {vecino}")

    print("\n--- Resultado Final ---")
    print("Dominios consistentes:", dominios)
    return dominios

# --- Ejecución ---
ac3_seguridad()
