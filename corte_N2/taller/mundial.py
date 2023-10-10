def campeones(listado):
    campeon={}
    for partidos in listado:
        if partidos[12]=='Final': 
            if (partidos[2]>partidos[4]) or (partidos[3]>partidos[5]):
                if partidos[0] not in campeon:
                    campeon[partidos[0]]= [partidos[16]]
                else:
                    year=campeon[partidos[0]]
                    year.append(partidos[16])
                    campeon[partidos[0]]=year
            else:
                if partidos[1] not in campeon:
                    campeon[partidos[1]]= [partidos[16]]
                else:
                    year=campeon[partidos[1]]
                    year.append(partidos[16])
                    campeon[partidos[1]]=year
    
    campeon=dict(sorted(campeon.items()))
    for equipo, year in (campeon.items()):
        print(f'{equipo}: {year}')

def subcampeones(listado):
    subcampeon={}
    for partidos in listado:
        if partidos[12]=='Final': 
            if (partidos[2]>partidos[4]) or (partidos[3]>partidos[5]):
                if partidos[1] not in subcampeon:
                    subcampeon[partidos[1]]= [partidos[16]]
                else:
                    year=subcampeon[partidos[1]]
                    year.append(partidos[16])
                    subcampeon[partidos[1]]=year
            else:
                if partidos[0] not in subcampeon:
                    subcampeon[partidos[0]]= [partidos[16]]
                else:
                    year=subcampeon[partidos[0]]
                    year.append(partidos[16])
                    subcampeon[partidos[0]]=year
    
    subcampeon=dict(sorted(subcampeon.items()))
    for equipo, year in (subcampeon.items()):
        print(f'{equipo}: {year}')


def participacion(listado):
    participantes={}
    for partido in listado:
        if partido[12]=='Group stage':
            

    



def main():
    f=open('wcm.csv','r',encoding="utf8")
    documento=f.readlines()
    f.close()
    lista=[]
    for dato in documento:
        lista.append(dato.rstrip('\n').split(','))
    a=campeones(lista)
    print(a)
    
def main2():
    f=open('wcm.csv','r',encoding="utf8")
    documento=f.readlines()
    f.close()
    lista=[]
    for dato in documento:
        lista.append(dato.rstrip('\n').split(','))
    a=subcampeones(lista)
    print(a)

def main3():
    f=open('wcm.csv','r',encoding="utf8")
    documento=f.readlines()
    f.close()
    lista=[]
    for dato in documento:
        lista.append(dato.rstrip('\n').split(','))
    a=participacion(lista)
    print(a)    


if __name__=="__main__":
    #main()
    #main2()
    main3()