def matrices(filas, columnas):
    matriz=[]
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            num=int(input(f'ingreseel numero de la posision [{i},{j}]:'))
            matriz[i].append(num)
    print(matriz)
    return matriz

if __name__=="__main__":
    filas=int(input('ingrese el numero de filas'))
    columnas=int(input('ingrese el numero de filas de columnas'))
    matrices(filas, columnas)