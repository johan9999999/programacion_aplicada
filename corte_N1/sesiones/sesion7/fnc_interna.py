import fnc_ext

def main():
    a=int(input('ingrese un numero'))
    b=int(input('ingrese otro numero'))
    r=fnc_ext.suma(a,b)
    print(r)
    print(f'ejecutado desde{__name__}') 

if __name__=="__main__":
    main()   