import random

# Incertidumbre usando probabilidad

# Probabilidad de que ocurra un evento (ej. que un sistema falle)
prob_fallo = 0.3

# Simulación de varios intentos
intentos = 10

for i in range(intentos):
    # Genera un número aleatorio entre 0 y 1
    r = random.random()

    # Si el número es menor que la probabilidad → ocurre el evento
    if r < prob_fallo:
        print(f"Intento {i+1}: FALLA")
    else:
        print(f"Intento {i+1}: FUNCIONA")