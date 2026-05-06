# Probabilidad condicionada y normalización

# F = fallo, ¬F = no fallo
# E = error detectado

# Probabilidades iniciales
P_F = 0.3
P_noF = 0.7

# Probabilidades condicionadas
P_E_dado_F = 0.9
P_E_dado_noF = 0.2

# Probabilidad conjunta (sin normalizar)
P_F_y_E = P_E_dado_F * P_F
P_noF_y_E = P_E_dado_noF * P_noF

# Normalización (para que las probabilidades sumen +1)
total = P_F_y_E + P_noF_y_E

P_F_dado_E = P_F_y_E / total
P_noF_dado_E = P_noF_y_E / total

print("P(Fallo | Error):", P_F_dado_E)
print("P(No fallo | Error):", P_noF_dado_E)