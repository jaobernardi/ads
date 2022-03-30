# Input getter
def get_input(message, set_type, tries=10, fail_return=None):
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
    return fail_return

def main():
    total = 0
    while valor := get_input("[!] Insira o valor: ", int, fail_return=-1):
        if valor == -1:
            break
        total += valor
    print(f"[!] Valor total: {total}")

if __name__ == "__main__":
    main()
    