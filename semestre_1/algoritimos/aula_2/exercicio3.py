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
    # Get inputs
    letterA = get_input("[?] Valor da variável A: ", float)
    letterC = get_input("[?] Valor da variável C: ", float) if letterA != None else None
    letterB = get_input("[?] Valor da variável B: ", float) if letterC != None else None

    if letterA != None and letterB != None and letterC != None:
        final_value = 4*letterA*letterC - letterB**2
        print(f"[!] Valor final será: {final_value}")

    else:
        print("[!] Falha ao processar os valores.")

if __name__ == "__main__":
    main()

