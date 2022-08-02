MATRICULA_AYESA = [1, 5, 5, 5, 9, 6]
MATRICULA_JOAO = [1, 9, 2, 2, 3, 4]

def somar_lista(lista):
    total = 0
    for index, value in enumerate(lista):
        if index % 2 == 0:
            continue
        total += value
    return total

def posicoes_zero(lista_1, lista_2):
    output = []
    for lista in [lista_1, lista_2]:
        for index, value in enumerate(lista):
            if value  == 0 and index not in output:
                output.append(index)
    output.sort()
    return output

def main():
    total_matriculas = somar_lista(MATRICULA_AYESA) + somar_lista(MATRICULA_JOAO)
    yield f'Soma: {total_matriculas}'
    total_zeros = posicoes_zero(MATRICULA_AYESA, MATRICULA_JOAO) or ['Nenhuma']
    yield "Posições com zero: "+(", ".join([str(i) for i in total_zeros]))

if __name__ == "__main__":
    for output in main():
        print(output)

