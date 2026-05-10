#Manuel Ponce 3° 3° Grupo C

'''Hacer un programa que permita el ingreso de nombres y los almacene en un archivo de texto con el nombre "nombres.txt".

El programa debe contar con un menú de opciones para permitir altas, listado y ordenamiento.

1) Alta de Nombres.
2) Listado de Nombres.
3) Ordenado de Archivo.
--------------------------------------
0) Salir

El ALTA de nombres implica agregar un nuevo nombre en el archivo.
El LISTADO de nombre el mostrar el contenido del archivo.
El ORDENADO implica realizar el ordenamiento del archivo, sin utilizar vectores o listas auxiliares, sino que se debe realizar directamente sobre el archivo.'''

def alta():
    arch=open('nombres.txt','a',encoding='utf-8')
    nom=input('\nIngrese Nombre: ').capitalize()
    if(len(nom)>0):
        arch.write(str(nom)+'\n')
    arch.close()

def mostrar():
    arch=open('nombres.txt','r',encoding='utf-8')
    aux=arch.readline()
    aux=aux[:-1]
    while(aux!=''):
        print(aux)
        aux=arch.readline()
        aux=aux[:-1]
    arch.close()
    
def ordenar():
    arch=open('nombres.txt','r',encoding='utf-8')
    a=int(0)
    for j in arch :
        a+=1
    arch.close()
    orde=open('ordenado.txt','w',encoding='utf-8')
    orde.close()
    for i in range(a):
        arch=open('nombres.txt','r',encoding='utf-8')
        orde=open('ordenado.txt','a',encoding='utf-8')
        temp=open('temporal.txt','w',encoding='utf-8')
        aux=int(0)
        p=''
        e=int(0)
        a=int(0)
        for c in arch :
            if(p==''):
                p=c
            if(c<p and c!=''):
                p=c
                a=e
            e+=1
                

        orde.write(p)
        arch.close()
        arch=open('nombres.txt','r',encoding='utf-8')
        e=int(0)
        for c in arch :
            if(e!=a):
                temp.write(c)
            e+=1

        arch.close()
        temp.close()
        arch=open('nombres.txt','w',encoding='utf-8')
        temp=open('temporal.txt','r',encoding='utf-8')
        
        for c in temp :
            arch.write(c)
        
        arch.close()
        orde.close()
        temp.close()
    arch=open('nombres.txt','w',encoding='utf-8')
    orde=open('ordenado.txt','r',encoding='utf-8')
    for i in orde :
        arch.write(i)
    arch.close()
    orde.close()

def menu_arch():
    aux2=int(0)
    arch=open('nombres.txt','r',encoding='utf-8')
    orde=open('ordenado.txt','w',encoding='utf-8')
    orde.close()
    c=arch.readline()
    if(c!=''):
        aux2=1
    aux=int(1)
    while(aux!=0):
        aux=int(input('\ningrese un numero en base a esta lista:\n 1) Alta de Empleado\n 2) Listado de Nombres\n 3) Ordenado de Archivo\n 0) Salir\n Ingrese: '))
        if(aux==1):
            alta()
            aux2=1
        elif(aux==2):
            if(aux2==1):
                mostrar()
            else:
                print('no puede mostrar una lista sin nombres')
        elif(aux==3):
            if(aux2==1):
                ordenar()
                ordenar()
            else:
                print('no se puede ordenar una lista sin nombres')
        elif(aux==0):
            print('FIN')
        else:
            print('Ese número no pertenece a ninguna acción')



arch=open('nombres.txt','a',encoding='utf-8')
orde=open('ordenado.txt','a',encoding='utf-8')
temp=open('temporal.txt','a',encoding='utf-8')
arch.close()
orde.close()
temp.close()
menu_arch()
