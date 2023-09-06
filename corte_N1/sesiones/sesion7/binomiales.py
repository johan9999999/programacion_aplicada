from factorial import factorial as f

def sss():
    n=int(input('ingrese el numero de elementos'))
    m=int(input('ingrese el por el numero de agrupaciones'))
    z=(f(n)/(f(m)*f(n-m)))
    print(f'el numero de combinaciones {z}')

if __name__=="__main__":
    sss()