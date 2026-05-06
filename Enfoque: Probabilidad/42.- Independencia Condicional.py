# Independencia condicional

# Eventos:
# L = lluvia, R = carretera mojada, N = nubes

# Probabilidades
P_L = 0.4
P_R_dado_L = 0.9
P_R_dado_noL = 0.1

P_N_dado_L = 0.8
P_N_dado_noL = 0.3

# Independencia condicional:
# R ⟂ N | L  → dado L, R y N son independientes

# Verificamos:
# P(R ∧ N | L) = P(R | L) * P(N | L)

P_RyN_dado_L = P_R_dado_L * P_N_dado_L

print("P(R y N | L):", P_RyN_dado_L)

# Caso sin lluvia (también independientes dado ¬L)
P_RyN_dado_noL = P_R_dado_noL * P_N_dado_noL

print("P(R y N | ¬L):", P_RyN_dado_noL)