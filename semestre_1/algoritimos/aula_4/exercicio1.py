from string import ascii_letters

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
    try:
        letterA, letterB, letterC, letterD = map(int, get_input("[!] Insira os valores separados por espaço: ", str).split())
    except ValueError:
        print("[!] Valores inválidos (falha ao receber valores do usuário)")
        return

    if letterB > letterC\
        and letterD > letterC\
        and (letterC+letterD) > (letterA+letterB)\
        and letterC > 0\
        and letterD > 0\
        and (letterA % 2) == 0:

        print("[!] Valores válidos")

    else:
        print("[!] Valores inválidos")

    pass

if __name__ == "__main__":
    main()