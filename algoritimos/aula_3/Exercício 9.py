# Detector de ano bissexto
# por João Lucas Bernardi | @jaobernardi | https://github.com/jaobernardi/

# Imports
from types import FunctionType
from typing import Any


# Input getter function
def filtered_input(text: str, to_type: Any, tries: int = 3) -> Any:
    """Get an input from the user and convert into a desired type.

    Args:
        text (str): Input text, will be passed to input()
        to_type (Any): Data type to wich input's output will be passed on.
        tries (int): How many tries before returning None. 
    """
    try_index = 0
    while try_index <= tries:
        # Add 1 to try index.
        try_index += 1
        try:
            # Get input and convert it
            output = input(text)
            output = to_type(output)
            # If the code above didn't fail, return the converted output
            return output
        except ValueError:
            # Continue if failed.
            continue
    # Give up and return none.
    return None


# Leap year detector
def is_leap_year(year: int):
    if year <= 0 or not isinstance(year, int):
        raise ValueError("Year cannot be negative or zero.")
    
    if (year % 4) == 0:
        return True
    return False


# Define main
def main():
    print("-"*10)
    print("[!] Detector de ano bissexto.")
    year = filtered_input("[?] Insira o ano: ", int)

    # Quit if input is invalid
    if year == None:
        print("{!!!} — Informações inválidas.")
        return

    try:
        if is_leap_year(year):
            print(f"[!] O ano {year} é bissexto.")
        else:
            print(f"[!] O ano {year} não é bisexto.")
    except ValueError:
        print("{!!!} — O ano não pode ser 0 ou negativo.")


if __name__ == "__main__":
    main()