def factorial(x):
    a=1
    for i in range (x):
        a*=i+1 #es igual i=a*i
    return(a)    
           



if __name__=="__main__":
    a=factorial(4)
    print(f'resultado {a}')