def encontrar_posiciones(a, b, inicio=0, resultado=[]):
    if inicio < len(a):
        if a[inicio:inicio + len(b)] == b:
            resultado.append(inicio)
        encontrar_posiciones(a, b, inicio + 1, resultado)

def main():
    a = input("Ingresa la cadena 'a': ")
    b = input("Ingresa la cadena 'b': ")

    posiciones = []
    encontrar_posiciones(a, b, 0, posiciones)

    if posiciones:
        print(f"Posiciones en las que se encuentra {b} en {a}: {posiciones}")
    else:
        print(f"{b} no se encuentra en {a}")

if __name__ == '__main__':
    main()
