print('figuras validas: \n',\
      '1. calcula el area de un circulo \n',\
          '2. rectangulo \n',\
               '3.triangulo')

A='NA'
fig=input('ingrese el nombre de la figura: ')

if(fig=='circulo'):
    r=int(input('ingrese el radio'))
    A=3.1416*r**2
elif(fig=='rectangulo'):
    b=int(input('ingrese la base'))
    h=int(input('ingrese la altura'))
    A=b*h
elif(fig=='triangulo'):
    b=int(input('ingrese la base'))
    h=int(input('ingrese la altura'))
    A=b*h/2
else:
    print('ingrese una opcion valida')
print('el valor de la base es', A)               

#lower=convierte el comentario a minuscula recibe cualquier forma en que se escriba
#upper=convierte el comentario a mayuscula 
#\n salto de linea