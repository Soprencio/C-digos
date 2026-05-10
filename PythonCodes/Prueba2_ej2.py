import random
def menu():
    a=int(0)
    b=int(0)
    while(a!=5):
        a=int(input('ingrese un numero en base a esta lista para llevar a cabo una de las siguientes opciones\n 1) Generar y Cargar Vector\n 2) Mostrar Vector\n 3) Ordenar Vector\n 4) Desordenar Vector\n 5)Salir\n ingrese:'))
        if(a==1):
            b+=1
            generar_cargar(b)
        elif(a==2):
            if(b==0):
                print('el vector que desea mostrar no existe')
            else:
                mostrar_vec()
        elif(a==3):
            if(b==0):
                print('el vector que desea ordenar no existe')
            else:
                ordenar_vec()
        elif(a==4):
            if(b==0):
                print('el vector que desea desordenar no existe')
            else:
                desordenar_vec()
        elif(a==5):
            print('fin')
        else:
            print('ese numero no corresponde a ninguna opcion')

def generar_cargar(b):
    if(b==1):
        for i in range(30):
            vec[i]=random.randint(0,9)
    else:
        for i in range(30):
            vec[i]=random.randint(0,9)

def mostrar_vec():
    print(vec)

def ordenar_vec():
    for i in range(len(vec)-1):
        for j in range(i+1,len(vec)):
            if(vec[i]<vec[j]):
                aux=vec[i]
                vec[i]=vec[j]
                vec[j]=aux

def desordenar_vec():
    for i in range(len(vec)):
        f=random.randint(0,29)
        aux=vec[i]
        vec[i]=vec[f]
        vec[f]=aux

vec=[None]*30
menu()
