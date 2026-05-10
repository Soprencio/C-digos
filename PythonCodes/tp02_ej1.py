#Ponce Manuel 3º 3º Grupo C

'''Hacer un codigo que permita el ingreso de un valor numérico entero y muestre si ese valor es o no un número primo.'''

a=int(input('ingrese a:'))
b=int(0)
for c in range(2,a-1):
    if(a%c==0):
        b+=1
if(b==0):
    print(a,'es un numero primo')
else:
    print(a,'no es un numero primo')
