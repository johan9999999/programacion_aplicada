import random as r
def xtz():
    pal=''
    nombre='johan'
    while pal !='exit':
        #x=r.randint(100,180)
        x=r.choice(nombre)
        print(x)
        pal=input('escriba exit para salir')

if __name__=="__main__":
    xtz()