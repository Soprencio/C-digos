#Manuel Ponce 3° 3°

'''Hacer un programa que permita generar de un número de cuatro dígitos distintos entre si y los almacene en una cadena de caracteres. Ese número generado será
el número que tendremos que adivinar.

El programa deberá solicitar al usuario que ingrese un número de hasta cuatro dígitos y deberá devolver la información sobre los números ingresados y suestado. 
'''

def parecidos(a,b):
    e=int(0)
    f=int(0)
    g=int(0)
    aux=''
    for c in range(0,4):
        j=int(0)
        while(a[c]!=b[j]and j<3):
            j+=1
        if(a[c]==b[j]):
            if(c==j):
                e+=1
            else:
                f+=1
        else:
            g+=1
    
    return(aux+str(e)+'B'+str(f)+'R'+str(g)+'M')

def numero_esta(x,n):
    for i in range(len(x)):
        if(str(n)==x[i]):
            return(True)
    return(False)
    
def generar_num():
    import random
    x=''
    for c in range(4):
        n=random.randint(0,9)
        while(numero_esta(x,n)):
              n=random.randint(0,9)
        x+=str(n)
    return(x)

def intentos(b):
    aux2='4B0R0M'
    for c in range(10):
        a=str(input('ingrese una cadena de 4 números distintos entre si:'))
        print(parecidos(a,b))
        if(parecidos(a,b)==aux2):
            return(True)
    return(False)
            
b=generar_num()

if(intentos(b)):
    print('felicitaciones, has adivinado el numero')
else:
    print('que mal... no has logrado adivinar el numero',b,'en menos de 10 intentos')
