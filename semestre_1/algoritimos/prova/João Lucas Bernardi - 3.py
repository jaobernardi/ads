# Programa 3 - João Lucas Bernardi (https://github.com/jaobernardi)

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

def main():
    products = {
        1: {
            "name": "Cachorro Quente",
            "price": 10.50
        },
        2: {
            "name": "X-Salada",
            "price": 16.50
        },
        3: {
            "name": "Torrada Simples",
            "price": 6.70
        },
        4: {
            "name": "Refrigerante",
            "price": 5.00
        },
    }

    print("Cód - Produto - Preço")
    for cod, data in products.items():
        print(f"{cod} - {data['name']} - R${data['price']}")
    print("Faça seu pedido", "-"*25)

    pedido = []

    while True:
        product_code = get_input("Informe o código do produto ou [-1] para finalizar: ", int)
        if product_code == -1:
            break
        pedido.append(product_code)
    print("PEDIDO FECHADO", "-"*25)
    valor_total = sum([products[i]['price'] for i in pedido])
    print(f"Valor total: R$ {valor_total}")

if __name__ == "__main__":
    main()