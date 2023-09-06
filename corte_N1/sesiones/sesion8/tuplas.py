def app(a,*args,**kwargs):
    print(args)
    print(a)
    print(kwargs)


if __name__=="__main__":
    app(1,2,5,3,6,x=45,b=78)

    # *args es para reunir datos(solo numeros)
    #si pongo las variables las cogen uno a uno
    #kwargs es para datos con variables definidas
    #tupla (imprime secuencia de numeros)