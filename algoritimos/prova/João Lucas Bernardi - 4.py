# Programa 4 - João Lucas Bernardi (https://github.com/jaobernardi)

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
    cotacoes = []

    for i in range(3):
        index = i + 1
        cot = get_input(f"Cotação {index}: R$ ", int)
        cotacoes.append(cot)
    
    minimal = min(cotacoes)
    trues = [False, False, False]
    minimal_index = 0
    for i in range(len(cotacoes)):
        if cotacoes[i] == minimal:
            minimal_index = i+1
            trues[i] = True
    
    if all(trues):
        print("Não foi possível encontrar o menor valor.")
        return
    
    print(f"Menor valor foi o {minimal_index}: {minimal}")

if __name__ == "__main__":
    main()