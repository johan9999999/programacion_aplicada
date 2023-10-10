def main_read3():
    f=open('wcm.csv','rt')
    documento=f.readlines()
    f.close()
    lista=[]
    for dato in documento:
        lista.append(dato.rstrip('\n').split(','))
    print(lista)

if __name__ == "__main__":
    main_read3()
