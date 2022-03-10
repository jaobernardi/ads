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


# Define the main function
def main():
    # Get the height
    salAtual = get_input("[?] Escreva o seu salário: ", float)
    # Don't bother getting the sales total if the salary is invalid.
    salVendas = get_input("[?] Escreva o total de vendas: ", float) if salAtual != None else None
    # Check if both values are valid
    if salAtual != None and salVendas != None:
        salFinal = salAtual
        salComissao = 0
        if salVendas >= 100000:
            salComissao = (5 * (salVendas/100))
            salFinal += salComissao
        print(f"[!] Salário final é de R$ {salFinal} e a comissão será de R$ {salComissao}")
    else:
        print("[!] Salário ou Reajuste inválidos.")


# Prevent running main if this is imported.
if __name__ == "__main__":
    # Run the code
    main()
