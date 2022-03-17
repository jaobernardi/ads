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
    letterX = get_input("[?] Valor de X: ", float)
    letterY = get_input("[?] Valor de Y: ", float) if letterX != None else None
    letterZ = get_input("[?] Valor de Z: ", float) if letterY != None else None
    final = 0
    if letterX and letterY and letterZ != None:

        if (letterX > letterY or letterZ <= 20):
            final = letterX * 2
        else:
            letterX = letterX/2
            letterZ = letterZ/5
            final = sum([letterX, letterZ])

        print(f"[!] Resultado final: {final}")
        print(f"[!] X: {letterX}, Y: {letterY}, Z: {letterZ}")
        return

    print("[!] Valor inválidos (falha ao processar)")
if __name__ == "__main__":
    main()