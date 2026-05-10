#Manuel Ponce 3° 3° Grupo C

'''
Hacer un programa que permita crear dos vectores de 30 elementos cada uno, donde se almacenarán las temperaturas máximas y mínimas, ambos valores con decimales entre 0.0 y 45.0,
utilizar uniform() de la biblioteca de random, y muestre:

-La mayor temperatura mínima.
-La mayor temperatura máxima.
-Las temperaturas máximas y mínimas promedio.'''

import random

def corroborar(i):
    while(vec_min[i]>=vec_max[i]):
        vec_min[i]=random.uniform(0.0,44.9)
        vec_max[i]=random.uniform(0.1,45.0)
        
def valores():
    e=int(0)
    f=int(0)
    aux3=int(0)
    aux4=int(0)
    for i in range(30):
        vec_min[i]=random.uniform(0.0,45.0)
        vec_max[i]=random.uniform(0.0,45.0)
        corroborar(i)
        if(vec_min[i]>f):
            f=vec_min[i]
        if(vec_max[i]>e):
            e=vec_max[i]
        aux3+=vec_min[i]
        aux4+=vec_max[i]
    resultados(f,e,aux3,aux4)

def resultados(f,e,aux3,aux4):
    aux3/=30
    aux4/=30
    print('el promedio de temperatura mínima es de',aux3)
    print('el promedio de temperatura maxima es de',aux4)
    print('la temperatura minima mas alta fue de',f)
    print('la temperatura maxima mas alta fue de',e)

vec_min=[None]*30
vec_max=[None]*30
valores()
