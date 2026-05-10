#Manuel Ponce 3º 3º Grupo C

'''Hacer un programa que permita mostrar todos los números primos que existan entre dos valores enteros ingresados por el usuario, y muestre también el total de números primos
encontrados. Implementando una función de nombre es_primo(n) que devuelve verdadero o falso según sea primo o no.'''

def es_primo(c):
    p=int(0)
    for d in range(2,c-1):
        if(c%d==0):
            p+=1
    if(p==0):
        if(c!=1):
            return(True)
        return(False)
    return(False)
a=int(input('ingrese a:'))
b=int(input('ingrese b:'))
e=int(0)
for c in range(a,b):
    if(es_primo(c)):
           print(c,end=' ')
           e+=1
print('\nhay',e,'primos')
