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
    return exit(1)


def fatorial(n):
    output = n or 1
    while n >= 0:
        output *= (n-1 if n-1 > 0 else 1)
        n -= 1
    return output


def fatorial_recursivo(n):
    if n <= 0: return 1
    return fatorial_recursivo(n-1) * n


def main():
    number = get_input('[Com loops explícitos] -> ', cast_type=int)
    yield fatorial(number)

    number = get_input('[Com recursividade] -> ', cast_type=int)
    yield fatorial_recursivo(number)

if __name__ == "__main__":
    for output in main():
        print(output)