import sys

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

def check_version():
    version = sys.version_info
    if version.major != 3 or version.minor <= 10:
        print("[!] Não será possível executar esse código pois a versão do seu intepretador é inferior à 3.10.")
        sys.exit(0)

def main():
    gas_types = {
        'D': {'price': 5.499, 'name': 'Diesel'},
        'G': {'price': 6.369, 'name': 'Gasolina'}
    }
    gas_type = get_input(f"[?] Qual o tipo de combustível? {[i for i in gas_types]}: ", str)    
    quantity = get_input("[?] Qual a quantidade de combustível (litros): ", float)
    
    if not quantity:
        print("[!] Valor informado é inválido.")
        return
    
    # Allow to implement different calculations to each type
    match gas_type.upper():
        case 'D':
            per_liter_value = gas_types['D']['price']
            if quantity > 20:
                per_liter_value = per_liter_value-(per_liter_value/100)*5
            else:
                per_liter_value = per_liter_value-(per_liter_value/100)*3

        case 'G':
            per_liter_value = gas_types['G']['price']
            if quantity > 20:
                per_liter_value = per_liter_value-(per_liter_value/100)*6
            else:
                per_liter_value = per_liter_value-(per_liter_value/100)*4

        case _:
            if gas_type.upper() not in gas_types:
                print("[!] Tipo de combustível não categorizado.")
                return

            print("[!] Erro: O tipo de combustível é valido, todavia, um método específico para ele ainda não foi implementado.")
            return

    # Calc final
    print(f"[!] Valor final: R$ {round(per_liter_value*quantity*1000)/1000}")


if __name__ == "__main__":
    check_version()
    main()
