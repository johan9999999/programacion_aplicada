n=int(input('ingrese la cantidad de numeros solicitados '))
x=1;num=2
numero='1 '
while x<n:
    for i in range(2,num+1):
        primo=num%i
        if (primo==0 and num==i):
            numero+=str(f'{num} ')
            num+=1
            x+=1
        elif(primo==0 and num!=i):
            num+=1
            break
print(numero)