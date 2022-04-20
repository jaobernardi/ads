# Programa 1 - João Lucas Bernardi (https://github.com/jaobernardi)

def get_input(message, cast_type, tries: int = 1):
    """Forma fácil de adiquirir o input do usuário
    ---
    Args:
        message (str)
        cast_type (Any)
        tries (int)
    """
    while tries >= 0:
        # Get input
        inp = input(message)
        try:
            # Return the typed input
            return cast_type(inp)
        except ValueError:
            # Remove 1 try and continue
            tries -= 1
    # Return none if there was no successful input.
    return None


def main():
    # Get info from user
    time_spent = get_input("Quantos dias o carro ficou alugado: ", int)
    # Don't bother getting Km if time_spent is invalid.
    km_spent = get_input("Quantos Km foram rodados: ", int) if time_spent else None

    # Taxes
    per_km = 0.15
    per_day = 60.0

    print("-"*25)

    if time_spent and km_spent:
        # Calculate final prices.
        time_spent_money = time_spent * per_day
        km_spent_money = km_spent * per_km
        
        print((
            f"Valor gasto com a diária do carro:  {time_spent_money}\n"
            f"Valor gasto com Km rodado:  {km_spent_money}\n"
            f"Valor total a pagar:  {time_spent_money+km_spent_money}"
        ))
        return
    print("Valores inválidos.")

if __name__ == "__main__":
    main()