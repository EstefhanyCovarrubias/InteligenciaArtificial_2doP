# Red bayesiana simple: Lluvia → Césped mojado

# Probabilidades
P_Lluvia = 0.3
P_noLluvia = 0.7

# Probabilidades condicionadas
P_Mojado_dado_Lluvia = 0.9
P_Mojado_dado_noLluvia = 0.2

# Probabilidad total de que el césped esté mojado
P_Mojado = (P_Mojado_dado_Lluvia * P_Lluvia) + \
           (P_Mojado_dado_noLluvia * P_noLluvia)

# Regla de Bayes para invertir la relación
P_Lluvia_dado_Mojado = (P_Mojado_dado_Lluvia * P_Lluvia) / P_Mojado

print("P(Césped mojado):", P_Mojado)
print("P(Lluvia | Césped mojado):", P_Lluvia_dado_Mojado)