def calcular_divisores(numero):
    return [i for i in range(1, numero) if numero % i == 0]

def es_numero_perfecto(numero):
    return sum(calcular_divisores(numero)) == numero

# Solicitar al usuario la cantidad de números perfectos deseados (hasta un máximo de 10)
cantidad_perfectos = min(int(input("Ingrese la cantidad de números perfectos que desea encontrar (hasta 10): ")), 10)

# Encontrar y mostrar los números perfectos
encontrados = 0
numero = 1

while encontrados < cantidad_perfectos:
    if es_numero_perfecto(numero):
        print(numero, "es un número perfecto.")
        encontrados += 1
    numero += 1
