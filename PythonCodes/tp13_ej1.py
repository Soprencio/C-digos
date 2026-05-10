#Manuel Ponce 3° 3° Grupo C

'''Hacer un programa que permita crear una matriz de 10 filas por 10 columnas, debiendo cargar la primera fila y la primera columna con valores del 0 al 9 consecutivos y ordenados
y mostrar la matriz en forma de matriz.
Luego completar la matriz con la multiplicación de los elementos de la primera fila con los elementos de la primera columna.'''

import time

def pre_mostrar():
    print('\033[2J\033[1;1f')
    j=int(0)
    for i in range(10):
        print('\033[30;41m')
        mat[j][i]=i
        print('\033['+str(j+1)+';'+str((i+1)*5)+'H',mat[j][i])
        time.sleep(.5)
        mat[i][j]=i
        print('\033['+str(i+1)+';'+str((j+1)*5)+'H',mat[i][j])
        time.sleep(.5)

def mostrar():
    for f in range(1,10):
        for c in range(1,10):
            print('\033['+str(f+1)+';'+str((c+1)*5)+'H',mat[f][c])
            print('\033[30;42m')
            print(mat[0][c])
            print(mat[f][0])
            time.sleep(.5)
            print('\033['+str(f+1)+';'+str((c+1)*5)+'H',mat[f][c])
            print('\033[0;m')
            print(mat[0][c])
            print(mat[f][0])
            

def tabla():
    for f in range(1,10):
        for c in range(1,10):
            mat[f][c]=mat[f][0]*mat[0][c]

mat=[[0,1,2,3,4,5,6,7,8,9],
     [1,0,0,0,0,0,0,0,0,0],
     [2,0,0,0,0,0,0,0,0,0],
     [3,0,0,0,0,0,0,0,0,0],
     [4,0,0,0,0,0,0,0,0,0],
     [5,0,0,0,0,0,0,0,0,0],
     [6,0,0,0,0,0,0,0,0,0],
     [7,0,0,0,0,0,0,0,0,0],
     [8,0,0,0,0,0,0,0,0,0],
     [9,0,0,0,0,0,0,0,0,0]]
tabla()
pre_mostrar()
mostrar()

