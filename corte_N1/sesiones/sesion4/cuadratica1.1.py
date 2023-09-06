a = float(input("Ingrese el coeficiente a: "))
b = float(input("Ingrese el coeficiente b: "))
c = float(input("Ingrese el coeficiente c: "))

if discriminante >= 0:
    x1 = (-b +( b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    print("Solución 1:", x1)
    print("Solución 2:", x2)
else:
    print("Su respuesta es imaginaria")
