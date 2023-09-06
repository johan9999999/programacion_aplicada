n = int(input("Ingrese la cantidad de números de Fibonacci que desea mostrar: "))

a, b = 0, 1

print("Los primeros", n, "números de Fibonacci son:")
for _ in range(n):
    print(a)
    a, b = b, a + b
