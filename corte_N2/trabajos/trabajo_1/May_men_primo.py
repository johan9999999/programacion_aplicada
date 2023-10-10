from random import randint as r

def generar_lista():
    numeros_aleatorios = []
    for _ in range(10):
        numeros_aleatorios.append(r(1, 50))
    return numeros_aleatorios

def mayor(lista):
    mayor_numero = lista[0]
    for numero in lista:
        if numero > mayor_numero:
            mayor_numero = numero
    return mayor_numero

def minimo(lista):
    minimo_numero = lista[0]
    for numero in lista:
        if numero < minimo_numero:
            minimo_numero = numero
    return minimo_numero

def es_primo(numero):
    if numero <= 1:
        return False

    es_primo_result = True 

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            es_primo_result = False  
            break

    return es_primo_result

def primos(lista):
    numeros_primos = []
    for numero in lista:
        if es_primo(numero):
            numeros_primos.append(numero)
    return numeros_primos

if __name__ == "__main__":
    lista_1= generar_lista()
    print("Lista :", lista_1)
    
    maximo_numero = mayor(lista_1)
    print("Número mayor:", maximo_numero)
    
    minimo_numero = minimo(lista_1)
    print("Número menor:", minimo_numero)
    
    numeros_primos = primos(lista_1)
    print("Números primos en la lista:", numeros_primos)
