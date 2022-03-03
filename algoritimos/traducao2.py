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
    # Don't bother getting the reajuste if the salary is invalid.
    salReajuste = get_input("[?] Escreva o reajuste: ", float) if salAtual else None
    # Check if both values are valid
    if salAtual and salReajuste:
        salFinal = (salAtual * (salReajuste/100)) + salAtual
        print(f"[!] Salário final é de R$ {salFinal}")
    else:
        print("[!] Salário ou Reajuste inválidos.")


# Prevent running main if this is imported.
if __name__ == "__main__":
    # Run the code
    main()
