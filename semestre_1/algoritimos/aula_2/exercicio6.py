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
    number = get_input("[!] Informe um número: ", int)

    if number != None:
        if number > 0:
            print("[!] Este número é positivo")
        elif number < 0:
            print("[!] Este número é negativo")
        else:
            print("[!] Este número é neutro.")
        return
    print("[!] Número inválido (falha ao processa entrada)")

if __name__ == "__main__":
    main() 