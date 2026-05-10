#Ponce Manuel 3º 3º Grupo C

'''Existen un tipo de número que se denomina número perfecto. Estos números son los que la suma de sus divisores, menos si mismo, da el mismo número.
Ejemplo: el número 6 tiene como divisores al 1, al 2, al 3 y al 6. Si sumamos los divisores menos si mismo tenemos 1 + 2 + 3 = 6.
Hacer que codigo que permita ingresar un valor entero y que diga si es o no un numero perfecto'''


a=int(input('ingrese a:'))
b=int(0)
for c in range(1,a-1):
    if(a%c==0):
        b+=c
if(a==b):
    print(a,'es un numero perfecto')
else:
    print(a,'no es un numero perfecto')
