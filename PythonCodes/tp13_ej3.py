#Manuel Ponce 3° 3° Grupo C

'''
Hacer un programa que permita el ingreso de la cantidad de filas y columnas, para la creación de una matriz.
Cargar la matriz con valores elegidos al azar en un rango también ingresado por el usuario.
Se pide hacer un menú con las siguientes opciones:

1 - Crear Matriz
2 - Cargar Matriz
3 - Mostrar Matriz
4 - Ordenar Matriz Completa
5 - Ordenar Matriz por Columnas
6 - Ordenar Matriz por Filas
0 - Salir.

Donde para el punto (4) ordena de mayor a menor, para el (5) las columnas de menor a mayor y para el (6) las filas de mayor a menor.

Se pide:
Implementar funciones para cada tarea.
Los ordenamientos deben realizarse sobre la misma matriz.
El contenido de la matriz, debe mostrarse en forma de matriz.'''

import random
def menu():
    op=int(-1)
    h=int(0)
    while(op!=0):
        op=int(input('\ningrese un numero de esta lista para llevar a cabo una de estas acciones\n 1° Crear Matriz\n 2° Cargar Matriz\n 3° Mostrat Matriz\n 4° Ordenar Matriz Completa\n 5° Ordenar Matriz por columnas\n 6° Ordenar Matriz por filas\n 0° Salir\n Ingrese:'))
        if(op==1):
            h+=1
            if(h==1):
                mat,f,c=crear_mat()
            else:
                print('ya se creo la matriz\n')
        elif(op==2):
            if(h!=0):
                cargar_mat(mat,f,c)
            else:
                print('todavia no se a creado una matriz\n')
        elif(op==3):
            if(h!=0):
                mostrar_mat(mat,f,c)
            else:
                print('todavia no se a creado una matriz\n')
        elif(op==4):
            if(h!=0):
                ordenar_com_mat(mat,f,c)
            else:
                print('todavia no se a creado una matriz\n')
        elif(op==5):
            if(h!=0):
                ordenar_c_mat(mat,f,c)
            else:
                print('todavia no se a creado una matriz\n')
        elif(op==6):
            if(h!=0):
                ordenar_f_mat(mat,f,c)
  
def crear_mat():
    aux=[]
    f=int(input('ingrese la cantidad de filas:'))
    c=int(input('ingrese la cantidad de columnas:'))
    aux=[None] * f
    for i in range(f):
        aux[i]=[None] * c
    return(aux,f,c)


def cargar_mat(mat,f,c):
    a=int(input('ingrese desde que numero se generaran los valores:'))
    b=int(input('ingrese hasta que numero se generaran los valores:'))
    for i in range(f):
        for j in range(c):
            mat[i][j]=random.randint(a,b)

def mostrar_mat(mat,f,c):
    print('\033[2J\033[1;1f')
    for i in range(f):
        for j in range(c):
            print('\033['+str(i+1)+';'+str((j+1)*5)+'H',mat[i][j])
    for i in range(f):
        for j in range(c):
             print(mat[i][j],end=' ')
        print()

def ordenar_com_mat(mat,f,c):
    for i in range(f):
        for j in range(c):
            for g in range(f):
                for k in range(c):
                    if(mat[i][j]>mat[g][k]):
                        aux=mat[i][j]
                        mat[i][j]=mat[g][k]
                        mat[g][k]=aux

def ordenar_c_mat(mat,f,c):
    for j in range(c):
        for i in range(f-1):
            for g in range(i+1,f):
                if(mat[i][j]>mat[g][j]):
                    aux=mat[i][j]
                    mat[i][j]=mat[g][j]
                    mat[g][j]=aux

def ordenar_f_mat(mat,f,c):
    for j in range(f):
        for i in range(c-1):
            for g in range(i+1,c):
                if(mat[j][i]<mat[j][g]):
                    aux=mat[j][i]
                    mat[j][i]=mat[j][g]
                    mat[j][g]=aux
      
menu()
print('fin')
