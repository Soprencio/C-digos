#Manuel Ponce 3º 3º Grupo C

'''Hacer un programa que permita indicar si dos números son los denominados números amigos. Los números amigos son aquellos donde la sumade los divisores de uno, menos si
mismo, da como resultado el otro número y viceversa. Implementar la función es_amigo(a, b) que devuelve verdadero o falso según sea amigo o no.'''

def es_amigo(a,b):
    e=int(0)
    d=int(0)
    for c in range(1,a-1):
        if(a%c==0):
            e+=c

    for c in range(1,b-1):
        if(b%c==0):
            d+=c
    if(a==d and b==e):
        return(True)
    else:
        return(False)

a=int(input('ingrese a:'))
b=int(input('ingrese b:'))
if(es_amigo(a,b)):
    print(a,'y',b,'son numeros amigos')
else:
    print(a,'y',b,'no son numeros amigos')
