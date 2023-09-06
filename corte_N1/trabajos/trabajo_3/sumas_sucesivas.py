numero1 = int(input("Ingresa el primer número entero: "))
numero2 = int(input("Ingresa el segundo número entero: "))

resultado = 0

for i in range(numero1):
    resultado += numero2

print("El producto de", numero1, "y", numero2, "es:", resultado)
