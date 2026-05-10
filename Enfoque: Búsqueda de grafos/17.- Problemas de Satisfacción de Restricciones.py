# --- CSP: Problema de Satisfacción de Restricciones ---
# Variables: torres que necesitan frecuencia
# Dominios: bandas disponibles
# Restricciones: torres vecinas no pueden compartir la misma banda

# Variables
torres = ['T1', 'T2', 'T3']

# Dominios
bandas = ['Canal-700MHz', 'Canal-850MHz']

# Restricciones
restricciones = {
    'T1': ['T2'],
    'T2': ['T1', 'T3'],
    'T3': ['T2']
}

def comprobar_conflicto(torre, banda, plan):
    """Verifica si la torre puede usar la banda sin chocar con vecinos."""
    vecinos = restricciones.get(torre, [])
    for v in vecinos:
        if v in plan and plan[v] == banda:
            print(f"  [!] Conflicto: {torre} y {v} usan {banda}")
            return False
    return True

# --- Asignación de frecuencias ---
configuracion = {}
print("--- Configuración de Red CSP ---")

for torre in torres:
    for banda in bandas:
        print(f"Probando {banda} en {torre}...")
        if comprobar_conflicto(torre, banda, configuracion):
            configuracion[torre] = banda
            print(f"  [+] {torre} configurada.")
            break

# --- Resultado ---
print("\nPlan Final:")
for torre, banda in configuracion.items():
    print(f"{torre} -> {banda}")
