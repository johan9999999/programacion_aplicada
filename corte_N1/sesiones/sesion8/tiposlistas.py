def agregar(milista): #comentar
   num=int(input('que numero quiere agregar: '))
   milista.append(num)
   print(milista)


def inserta(milista):
    var=int(input('que valor desea agreagar'))
    idx=int(input('en que posicion'))
    milista.insert(idx,var)
    print(milista)

def borrar(milista):
    milista.clear()
    print(milista)   

def remover(milista):
    print(milista)
    var=int(input('numero que quiera remover: '))
    milista.remove(var)
    print(milista)      

def main():
    milista=[2,3,4,8]
    opc=''
    while opc!='exit':
        print('seleccione una opcion:\n',
          '1.agregar  \n 2. insertar\n 3. borrar')
        opc=input('=>')

        if opc=='1':
            agregar(milista)
        elif opc=='2':
            inserta(milista)  
        elif opc=='3':
            borrar(milista)
        elif opc=='4':
            re(milista)

if __name__=="__main__":
    main()
    