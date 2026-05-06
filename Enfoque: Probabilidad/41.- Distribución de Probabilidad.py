import random

# Distribución de probabilidad (evento discreto)
# Ejemplo: clima
# Estados posibles y sus probabilidades (suman 1)
estados = ["Soleado", "Nublado", "Lluvioso"]
probabilidades = [0.5, 0.3, 0.2]

# Verificación básica
print("Distribución de probabilidad:")
for e, p in zip(estados, probabilidades):
    print(f"{e}: {p}")

# Simulación usando la distribución
dias = 10

for i in range(dias):
    # Elegir un estado según su probabilidad
    estado = random.choices(estados, probabilidades)[0]
    print(f"Día {i+1}: {estado}")