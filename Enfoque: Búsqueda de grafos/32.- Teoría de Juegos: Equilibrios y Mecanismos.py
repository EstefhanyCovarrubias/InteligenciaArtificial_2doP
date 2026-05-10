def subasta_vickrey(ofertas):
    """Ejecuta una subasta Vickrey: el ganador paga el segundo precio."""
    # Ordenar ofertas de mayor a menor
    ordenadas = sorted(ofertas.items(), key=lambda x: x[1], reverse=True)

    ganador = ordenadas[0][0]          # mejor postor
    mejor_oferta = ordenadas[0][1]     # valor más alto
    segundo_precio = ordenadas[1][1]   # precio que realmente paga

    print("\n--- Subasta Vickrey ---")
    print("Ofertas:", ofertas)
    print("Ganador:", ganador)
    print("Paga:", segundo_precio)

# Ejemplo
ofertas = {
    'Agente1': 100,
    'Agente2': 80,
    'Agente3': 60
}

subasta_vickrey(ofertas)
