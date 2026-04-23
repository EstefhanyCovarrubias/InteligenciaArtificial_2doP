# Regla de Bayes - ejemplo con enfermedad

# Probabilidades iniciales
P_enfermedad = 0.01
P_no_enfermedad = 0.99

# Probabilidad del test
P_positivo_dado_enfermedad = 0.95
P_positivo_dado_no_enfermedad = 0.05

# Fórmula de Bayes
:contentReference[oaicite:0]{index=0}

# Probabilidad total de dar positivo
P_positivo = (P_positivo_dado_enfermedad * P_enfermedad) + \
             (P_positivo_dado_no_enfermedad * P_no_enfermedad)

# Probabilidad de tener la enfermedad dado positivo
P_enfermedad_dado_positivo = (P_positivo_dado_enfermedad * P_enfermedad) / P_positivo

print("P(Enfermedad | Test positivo):", P_enfermedad_dado_positivo)