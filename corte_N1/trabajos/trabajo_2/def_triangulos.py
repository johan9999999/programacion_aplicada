a = float(input("Ingresa la medida del primer lado: "))
b = float(input("Ingresa la medida del segundo lado: "))
c = float(input("Ingresa la medida del tercer lado: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("El triángulo es Equilátero")
    elif a == b or a == c or b == c:
        print("El triángulo es Isósceles")
    else:
        print("El triángulo es Escaleno")
else:
    print("No es un triángulo")

