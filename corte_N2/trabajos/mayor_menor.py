import random as r

def main(filas, columnas):
    matriz = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            num = r.randint(1, 10) 
            fila.append(num)
        matriz.append(fila)

    print("\nMatriz creada:")
    for fila in matriz:
        print(fila)

    maximo = max(matriz[0])
    minimo = min(matriz[0])

    for fila in matriz:
        max_fila = max(fila)
        min_fila = min(fila)
        if max_fila > maximo:
            maximo = max_fila
        if min_fila < minimo:
            minimo = min_fila

    print(f"\nNúmero más alto: {maximo}")
    print(f"Número más bajo: {minimo}")

    for i in range(len(matriz)):
        for j in range(len(matriz) - 1):
            if matriz[j][0] < matriz[j + 1][0]:
                matriz[j], matriz[j + 1] = matriz[j + 1], matriz[j]

    print("\nMatriz ordenada de mayor a menor:")
    for fila in matriz:
        print(fila)

if __name__ == "__main__":
    filas = int(input('Ingrese el número de filas: '))
    columnas = int(input('Ingrese el número de columnas: '))
    main(filas, columnas)