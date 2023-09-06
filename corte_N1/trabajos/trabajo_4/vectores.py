x1 = float(input("Ingrese la coordenada x del punto de origen: "))
y1 = float(input("Ingrese la coordenada y del punto de origen: "))
x2 = float(input("Ingrese la coordenada x del punto de destino: "))
y2 = float(input("Ingrese la coordenada y del punto de destino: "))

dx = x2 - x1
dy = y2 - y1

modulo = ((dx ** 2) + (dy ** 2)) ** 0.5

print(f"Las componentes rectangulares del vector son: dx = {dx}, dy = {dy}")
print(f"El módulo del vector es: {modulo}")
