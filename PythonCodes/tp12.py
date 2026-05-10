#Manuel Ponce 3° 3° Grupo C

'''En un vector de 30 elementos, generar valores elegidos al azar en un rango indicado por el usuario. Realizar una función que permita ordenar el vector de mayor a menor, no por
sus valores solamente sino que también según la frecuencia de aparición de los elementos.

El programa debe tener un menú con las siguientes opciones:

                                   1) Crear Vector.
                                   2) Cargar Vector.
                                   3) Mostrar Vector.
                                   4) Ordenar Vector.
                                   5) Desordenar Vector.
                                   0) Salir.'''
import random
def menu():    
    op=int(-1)
    a=int(0)
    h=int(0)
    while(op!=0):
        op=int(input('\ningrese un número en base a esta lista:\n 1° Crear Vector\n 2° Cargar Vector\n 3° Mostrar Vector\n 4° Ordenar Vector\n 5° Desordenar Vector\n 0° Salir\n Ingrese:'))
        if(op==1):
            a+=1
            crear_vec(a)
        elif(op==2):
            if(a>0):
                h+=1
                cargar_vec(h)
            else:
                print('todavia no se ha creado un vector\n')
        elif(op==3):
            if(a>0):
                mostrar_vec()
            else:
                print('todavia no se ha creado un vector\n')
        elif(op==4):
            if(a>0):
                orden_vec()
            else:
                print('todavia no se ha creado un vector\n')
        elif(op==5):
            if(a>0):
                desordenar_vec()
            else:
                print('todavia no se ha creado un vector\n')
        else:
            print('ese número no corresponde a ninguna funcion del menu')

def cargar_vecaux():
    for i in range(30):
        vecaux.append(0)
    

def desordenar_vec():
    for i in range(len(vec)):
        b=random.randint(0,9)
        for j in range(len(vec)):
            if(b==vec[j]):
                aux=vec[i]
                vec[i]=vec[j]
                vec[j]=aux
                
def crear_vec(a):
    if(a==1):
        print('\nse ha creado el vector\n')
    else:
        print('\nel vector ya a sido creado\n')

def cargar_vec(h):
    if(h==1):
        for i in range(30):
            vec.append(random.randint(0,9))
    else:
        for j in range(30):
            vec[j]=random.randint(0,9)
        
def orden_vecaux():
    for i in range(len(vecaux)-1):
        for f in range(i+1,len(vecaux)):
            if(vecaux[i]<vecaux[f]):
                aux=vecaux[i]
                vecaux[i]=vecaux[f]
                vecaux[f]=aux
                aux=vec[i]
                vec[i]=vec[f]
                vec[f]=aux

def descargar_vecaux():
    for i in range(len(vec)):
        vecaux[i]=0

def mostrar_vec():
    print(vec)

def orden_vec():
    for i in range(len(vec)):
        for j in range(len(vec)):
            if(vec[i]==vec[j]):
                vecaux[i]=vecaux[i]+1
        vecaux[i]=vecaux[i]+((vec[i]+1)/10)
    orden_vecaux()
    descargar_vecaux()

vec=[]
vecaux=[]
cargar_vecaux()
menu()
print('fin')
