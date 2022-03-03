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
    altura = get_input("[?] Escreva a altura: ", float)
    # Don't bother getting the width if the height is invalid.
    largura = get_input("[?] Escreva a largura: ", float) if altura else None
    # Check if both values are valid
    if altura and largura:
        area = altura * largura
        print(f"[!] A área é {area}")
    else:
        print("[!] Altura ou largura inválidos.")


# Prevent running main if this is imported.
if __name__ == "__main__":
    # Run the code
    main()