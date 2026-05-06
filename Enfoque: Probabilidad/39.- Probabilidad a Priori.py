import random

# Probabilidad a priori (creencia inicial sin evidencia)
# Ejemplo: clima
P_lluvia = 0.4
P_no_lluvia = 0.6

# Mostrar las probabilidades iniciales
print("Probabilidad a priori de lluvia:", P_lluvia)
print("Probabilidad a priori de no lluvia:", P_no_lluvia)

# Simulación basada en la probabilidad a priori
dias = 10

for i in range(dias):
    r = random.random()

    # Se decide solo con la probabilidad inicial (sin evidencia nueva)
    if r < P_lluvia:
        print(f"Día {i+1}: LLUVIA")
    else:
        print(f"Día {i+1}: NO LLUVIA")