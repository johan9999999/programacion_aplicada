import csv 

def main_read3():
    f=open('wcm.csv','rt')
    documento=f.readlines()
    print(documento)
    f.close()
   

if __name__=="__main__":
    main_read3()
    


