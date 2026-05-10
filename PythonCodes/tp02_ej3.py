#Ponce Manuel 3º 3º Grupo C

'''Otro tipo de número son los denominados números amigos. Los números amigos son aquellos donde la suma de los divisores de uno, menos si mismo, da como resultado el otro
número y viceversa. Ejemplo: los números 220 y 284, donde los divisores de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 que sumados dan 284 y los divisores de 284
son 1, 2, 4, 71, 142 que sumados dan 220.
Hacer un codigo que permita ingresar 2 valores enteros si que diga si son numeros amigos o no.'''

a=int(input('ingrese a:'))
b=int(input('ingrese b:'))
e=int(0)
d=int(0)
for c in range(1,a-1):
    if(a%c==0):
        e+=c

for c in range(1,b-1):
    if(b%c==0):
        d+=c
if(a==d and b==e):
    print(a,'y',b,'son numeros amigos')
else:
    print(a,'y',b,'no son numeros amigos')
    
