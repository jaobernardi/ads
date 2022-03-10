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
    # Get data
    number = get_input("[?] Informe o número: ", int)
    if number != None:
        # Check if number is 0 or is divisible by 2.
        if number == 0 or number % 2 == 0:
            print(f"[!] O número informado ({number}) é par")
            return
        # Display negative message
        print("[!] O número informado não é par.")
        return
    # Failed to process info
    print("[!] Falha ao processar as informações.")

if __name__ == "__main__":
    main()