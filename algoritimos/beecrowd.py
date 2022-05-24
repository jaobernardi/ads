from copy import copy

def gen_matriz(col, row):
    return [[0]*row]*col

if __name__ == "__main__":
    matriz = gen_matriz(12, 12)

    print(id(matriz[1]) == id(matriz[0]))




