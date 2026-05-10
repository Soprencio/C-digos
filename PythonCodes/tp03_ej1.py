#Ponce Manuel 3º 3º Grupo C

'''Hacer el codigo que permita ingresar el nombre de la materia y cuatro valores enteros que representan las notas de una materia, calcule el promedio e indique, Aprobado si
el promedio es mayor o igual que seis, Regular si el promedio es mayor o igual que cuatro y menor que seis, y Desaprobado si el promedio es menor que cuatro.'''

m=input('ingrese nombre de materia:')
a=int(input('ingrese la nota 1:'))
b=int(input('ingrese la nota 2:'))
c=int(input('ingrese la nota 3:'))
d=int(input('ingrese lo nota 4:'))
p=int(0)
p=(a+b+c+d)/4
if(p>=6):
    print('en la materia',m,'usted a aprobado')
else:
    if(p<=4):
        print('en la materia',m,'usted a reprobado')
    else:
        print('en la materia',m,'usted esta regular')
    
