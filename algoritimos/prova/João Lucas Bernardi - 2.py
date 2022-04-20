# Programa 2 - João Lucas Bernardi (https://github.com/jaobernardi)

def get_input(message, cast_type, tries: int = 1):
    """Forma fácil de adiquirir o input do usuário
    ---
    Args:
        message (str)
        cast_type (Any)
        tries (int)
    """
    while tries >= 0:
        # Get input
        inp = input(message)
        try:
            # Return the typed input
            return cast_type(inp)
        except ValueError:
            # Remove 1 try and continue
            tries -= 1
    # Return none if there was no successful input.
    return None

def count(start_n, end_n):
    div_three, pares, impares = 0, 1, 1       
    
    for i in range(start_n+1, end_n):
        if i % 3 == 0:
            div_three += 1
                
        if i % 2:
            pares += 1            
        else:
            impares +=1

        
    print(f"Divisivéis por 3: {div_three}")
    print(f"Pares: {pares}")
    print(f"Ímpares: {impares}")

def main():
    while True:
        # Get user input
        start_n = get_input("Informe um número inicial: ", int)
        end_n = get_input("Informe um número final: ", int) if start_n else None
        count(start_n, end_n)
        action = get_input("Informe [s] para repetir a operação ou [n] para encerrar: ", str)
        if action.lower() == "n":
            break

if __name__ == "__main__":
    main()