import typing
# Calculador de média ponderada.


# Input getter
def get_input(message, set_type, tries=10):
    while tries >= 0:
        # Get input
        inp = input(message)
        try:
            # Return the typed input
            return set_type(inp)
        except ValueError:
            # Remove 1 try and continue
            tries -= 1
    # Return none if there was no successful input.
    return None


def calculate_average(items: list):
    """
    Calculate the weighted average.

    Params:
        items: List.
    """
    bottom = 0
    top = 0 
    for v, w in items:
        bottom += w
        top += v*w
    return top/bottom


def main():
    items = []

    print("Calculador de média ponderada.")
    # Get how many values will be informed.
    amount = get_input("[?] Quantos items serão informados: ", int)
    if not amount:
        # Quit if it failed to get amount.
        print("Falha ao processar a quantidade de itens.")
        return
    
    # Get per item info.
    for index in range(amount):
        print("\n")  
        print(f"[!] Informações sobre o item #{index+1}")

        # Get item's info.
        value = get_input("[?] Valor do item: ", float)
        weight = get_input("[?] Peso do item: ", float) if value else None
        if not value and not weight:
            # Quit if info is trash
            print("Falha ao processar as informações do item.")
            return

        # Add it to the list
        items.append([value, weight])

    # Calculate the average
    total_value = calculate_average(items)
    print(f"[!] Média final será de: {total_value}")
    return


if __name__ == "__main__":
    main()