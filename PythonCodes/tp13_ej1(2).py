"""Ejercicio 1:
Hacer un programa que permita crear una matriz de 10 filas por 10 columnas, debiendo cargar la primera fila y la primera columna con valores del 0 al 9 consecutivos y
ordenados y mostrar la matriz en forma de matriz.Luego completar la matriz con la multiplicación de los elementos de la primera fila con los elementos de la primera columna."""

#Caballer Lucas - Grupo A


#Importaciones
import random

#Crear matriz
def crear_matriz(fi, co):
    m=[None]*fi
    for i in range(fi):
        m[i]=[None]*co
    return m

#Cargar matriz(primera fila y columna con valores del 0 al 9 consecutivos)
def cargar_matriz(m):
    for i in range(10):
        m[0][i]=i
        m[i][0]=i

def multiplicar(m,fi,co):
    for fila in range(1, fi):
        for columna in range(1, co):
            t=fila*columna
            m[fila][columna]=t
            t=0
            
            
                     

#Mostrar matriz
def mostrar_matriz(mat,fi,co):
    for fila in range(fi):
        for columna in range(co):
            print("{0:5d}".format(mat[fila][columna]), end=" ")
        print ()

        
#Llamado de funciones
mat=crear_matriz(10, 10)
cargar_matriz(mat)
multiplicar(mat,10,10)
mostrar_matriz(mat,10,10)

