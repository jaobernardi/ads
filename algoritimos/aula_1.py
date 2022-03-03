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
    # Print a welcome message
    print("Olá Mundo")
    
    # Get the age    
    age = get_input("Por favor, informe sua idade [número]: ", int)
    if not age:
        print("Não foi possível processar sua idade pois não é um número.")
        return

    print(f"Sua idade é de {age} anos.")


# Prevent running main if this is imported.
if __name__ == "__main__":
    # Run the code
    main()