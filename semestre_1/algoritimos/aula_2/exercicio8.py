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
    age = get_input("[?] Qual a idade: ", int)
    if age:
        if (age >= 5 and age <= 7):
            classificacao = "Infantil A"
        elif (age>= 8 and age <= 10):
            classificacao = "Infantil B"
        elif (age>= 11 and age <= 13):
            classificacao = "Juvenil A"
        elif (age>= 14 and age <= 17):
            classificacao = "Juvenil B"
        elif (age>= 18 and age <= 25):
            classificacao = "Adulto"
        else:
            classificacao = "indefinida, pois está fora da faixa determinada."
        print(f"[!] A classificação é {classificacao}")
        return
    print("[!] Inforamções inválidas")

if __name__ == "__main__":
    main()