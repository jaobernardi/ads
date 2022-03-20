# Input getter
import os


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
    A = get_input("", int)
    B = get_input("", int) if A else None
    if A and B:
        print(f"SOMA = {A+B}\n")
        return
    print("[!] Valores Inválidos")
    return

if __name__ == "__main__":
    os.system("cls")
    main()