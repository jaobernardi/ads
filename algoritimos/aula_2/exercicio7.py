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

def main():
    items = []

    print("Calculador de média ponderada.")
    # Get how many values will be informed.
    amount = get_input("[?] Quantos items serão informados: ", int)
    if not amount:
        # Quit if it failed to get amount.
        print("[!] Falha ao processar a quantidade de itens.")
        return
    
    # Get per item info.
    for index in range(amount):
        # Get item's info.
        value = get_input("[?] Valor do item: ", float)
        if value == None:
            # Quit if info is trash
            print("Falha ao processar as informações do item.")
            return

        # Add it to the list
        items.append(value)

    # Get the smallest
    min_value = min(items)
    print(f"[!] Menor número é: {min_value}")
    return


if __name__ == "__main__":
    main()