#Manuel Ponce 3° 3° Grupo C

'''Hacer un programa que permita resolver el siguiente problema:

Se realiza una encuesta a cinco personas, sobre dos bebidas gaseosas,donde se pide calificar sobre tres ítem (0-presentación, 1-sabor y 2-precio), utilizando
una valoración del uno al diez que deben generarse al azar.

Se deben calcular el promedio de aceptación que cada persona le dio a cada gaseosa y mostrar si la persona aprobó o no a la gaseosa, siendo que se da por
aprobada al tener una calificación mayor o igual que seis.'''

import random
def valoracion(x):
    e=int(0)
    f=int(0)
    for c in range(1,6):
        p=random.randint(1,10)
        s=random.randint(1,10)
        pr=random.randint(1,10)
    
        print('las valoraciones de la persona',c,'en la gaseosa',x,'fueron',p,'en la \npresentacion,',s,'en el sabor y',pr,'en el precio')
        print('la valoración promedio de la persona fue de',promedio(p,s,pr))
        if(promedio(p,s,pr)>=6):
            print('y por lo tanto su valoracion fue un aprobado\n')
        else:
            print('y por lo tanto su valoracion fue un desaprobado\n')

        if(promedio(p,s,pr)>e):
            e=promedio(p,s,pr)
            f=c
        if(c==5):
            print('el promedio mas alto de la gaseosa',x,'fue de',e,'segun la \npersona numero',f,'\n')
    
def promedio(p,s,pr):
    promedio=float(0)
    promedio=(p+s+pr)/3
    return(promedio)


a='Pepsi'
b='Coca-Cola'

valoracion(a)


valoracion(b)

       
    



    

    
