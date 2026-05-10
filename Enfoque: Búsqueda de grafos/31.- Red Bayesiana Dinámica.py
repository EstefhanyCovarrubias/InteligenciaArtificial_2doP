print("--- Sistema de Inferencia Climática Dinámica ---")

# --- Modelo de Transición ---
# Probabilidad de pasar de ayer a hoy (lluvia/viento)
def modelo_evolucion(lluvia_hoy, viento_hoy, lluvia_ayer, viento_ayer):
    p_lluvia = 0.7 if lluvia_ayer == lluvia_hoy else 0.3
    p_viento = 0.8 if viento_ayer == viento_hoy else 0.2
    return p_lluvia * p_viento

# --- Modelo de Observación ---
# Probabilidad de ver paraguas según clima
def verosimilitud(paraguas, lluvia, viento):
    if lluvia and viento:      p = 0.50
    elif lluvia and not viento: p = 0.90
    elif not lluvia and viento: p = 0.05
    else:                       p = 0.01
    return p if paraguas else (1.0 - p)

# --- Creencia inicial ---
# Distribución uniforme (no sabemos nada)
creencia = {(ll, vi): 0.25 for ll in [True, False] for vi in [True, False]}

def paso_dbn(creencia_pasada, evidencia):
    """Actualiza creencia: predicción + corrección + normalización."""
    nueva = {}
    for ll_h in [True, False]:
        for vi_h in [True, False]:
            # Predicción: suma de caminos posibles
            pred = sum(
                modelo_evolucion(ll_h, vi_h, ll_a, vi_a) * creencia_pasada[(ll_a, vi_a)]
                for ll_a in [True, False] for vi_a in [True, False]
            )
            # Corrección: incorporar evidencia
            nueva[(ll_h, vi_h)] = pred * verosimilitud(evidencia, ll_h, vi_h)
    # Normalización
    total = sum(nueva.values())
    return {estado: p / total for estado, p in nueva.items()}

# --- Simulación ---
observaciones = [True, True, False]  # Paraguas, Paraguas, No paraguas

for i, obs in enumerate(observaciones, 1):
    creencia = paso_dbn(creencia, obs)
    print(f"\nDía {i}: {'Paraguas' if obs else 'Sin paraguas'}")
    for (ll, vi), prob in sorted(creencia.items(), key=lambda x: x[1], reverse=True):
        clima = f"{'Lluvia' if ll else 'Seco'} & {'Viento' if vi else 'Calma'}"
        print(f"  {clima.ljust(15)}: {prob*100:5.2f}% {'█' * int(prob*20)}")
