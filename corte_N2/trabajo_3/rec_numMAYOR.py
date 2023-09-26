import random as r

def MAYOR (lista):
    if len(lista) == 1:
        return lista[0]
    max = MAYOR (lista[1:])
    if lista[0] > max:
        return lista[0]
    else:
        return max

def main():
    lista_num = [r.randint(1, 100) for i in range(10)]
    print("Lista aleatoria:", lista_num)
    resultado = MAYOR (lista_num)
    print("Resultado:", resultado)

if __name__ == '__main__':
    main()

