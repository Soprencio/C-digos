# Manuel Ponce 3° 3° Grupo C

'''Hacer un programa que permita el ingreso de la cantidad de filas y columnas, para la creación de una matriz, debiendo ser ambos valores iguales.
Cargar la matriz con valores elegidos al azar en un rango también ingresado por el usuario, de manera tal que todos los valores sean distintos.
Crear una segunda matriz, donde se almacenará la traspuesta de la matriz original, teniendo en cuenta que trasponer significa intercambiar las filas por las columnas.'''

import random
def matriz(f,c):
    a=int(input('ingrese desde donde van a ser generados los numeros:'))
    b=int(input('ingrese hasta donde van a ser generados los numeros:'))
    while(b-a<c*f):
        b=int(input('ingrese otro numero hasta el que puede llegar, el anterior era demasiado chico y no permitia que sean todos los numeros distintos:'))
    repeticion(a,b,c,f)

def crear(f,c):
    mat=[None]*f
    for i in range(f):
        mat[i]=[None]*c
    return(mat)

def repeticion(a,b,c,f):
    for i in range(f):
        for j in range(c):
            op=int(1)
            while(op>0):
                mat[i][j]=random.randint(a,b)
                op=int(0)
                for g in range(f):
                    for h in range(c):
                        if(i!=g or j!=h):
                            if(mat[i][j]==mat[g][h]):
                                op+=1
    mostrar(f,c)
    print()

def mostrar(f,c):
    print('\033[2J\033[1;1f')
    for i in range(f):
        for j in range(c):
            print('\033[30;42m')
            print('\033['+str(i+1)+';'+str((j+1)*5)+'H',mat[i][j])
    print('\033[0;m')

def giro(f,c):
    p=int(0)
    for j in range(f):
        for i in range(p,c):
            aux=mat[j][i]
            mat[j][i]=mat[i][j]
            mat[i][j]=aux
        p+=1
    mostrar(f,c)
    
f=int(input('ingrese la cantidad de filas y columnas:'))
c=f
mat=crear(f,c)
matriz(f,c)
giro(f,c)
