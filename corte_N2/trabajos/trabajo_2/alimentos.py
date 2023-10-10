def obtener_producto_por_codigo(codigo, lista_productos):
    for producto in lista_productos:
        if producto[0] == codigo:
            return producto[1], float(producto[2])  
    return () 

def main_read3():
    f = open('Alimentos.txt', 'rt')
    documento = f.readlines()
    f.close()
    lista_productos = []
    for dato in documento:
        lista_productos.append(dato.rstrip('\n').split(','))
    print(lista_productos)
    codigo_buscar = input("Ingresa el código del producto: ")

    descripcion, tarifa_iva = obtener_producto_por_codigo(codigo_buscar, lista_productos)

    if descripcion:
        print(f'Descripción: {descripcion}')
        print(f'Tarifa IVA: {tarifa_iva}')

        cantidad_producto = float(input("Ingresa la cantidad del producto: "))

        valor_producto_sin_iva = cantidad_producto * (1 + tarifa_iva)
        valor_iva = cantidad_producto * tarifa_iva

        print(f'Valor del Producto sin IVA: {valor_producto_sin_iva}')
        print(f'Valor del IVA: {valor_iva}')
    else:
        print(f'El código {codigo_buscar} no se encontró en la lista de productos.')

if __name__ == "__main__":
    main_read3()
