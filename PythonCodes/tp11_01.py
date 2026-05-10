#Manuel Ponce 3° 3° Grupo C
'''
°Hacer un programa que permita crear un vector con la cantidad de elementos ingresados por el usuario, debiendo generar al azar valores en un rango también ingresado por el
usuario, es decir, entre dos valores.

°Se pide mostrar el vector generado, luego ordenarlo de mayor a menor, y volver a mostrar el vector.

°Luego mostrar los elementos del vector indicando cuántas veces se repiten, teniendo en cuenta que si el valor que se encuentra solo una vez, está repetido cero veces.'''

import random
def orden():
    for i in range(len(vec)-1):
            for f in range(i+1,len(vec)):
                if(vec[i]<vec[f]):
                    aux=vec[i]
                    vec[i]=vec[f]
                    vec[f]=aux
                    
def numeros(a):
    for d in range(a):
        vec[d]=random.randint(b,c)
        
def numer_dos(a):
    for d in range(a):
        vec2[d]=-1

def buscar():
    for i in range(len(vec)):
        for j in range(len(vec)):
            if(vec[i]==vec[j]):
                vec2[i]+=1

def buscado():
    for i in range(len(vec)):
        if(vec2[i]>-1):
            print('el numero en la posición',i,'del vector se repite',vec2[i],'veces')
            
a=int(input('Ingrese la cantidad de elementos:'))
b=int(input('Ingrese desde que valor se pueden generar los númreros:'))
c=int(input('Ingrese hasta que valor se pueden generar los números:'))
vec2=[None]*a
vec=[None]*a
numer_dos(a)
numeros(a)
print(vec)
orden()
print(vec)
buscar()
print(vec2)
buscado()
