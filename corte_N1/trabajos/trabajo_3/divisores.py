
numero = int(input("Ingresa un número: "))


if numero == 0:
    print("Ningún número es divisible entre cero")
else:
    print("Los divisores positivos de", numero, "son:")

    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
