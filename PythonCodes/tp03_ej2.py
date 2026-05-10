#Ponce Manuel 3º 3º Grupo C

'''Hacer el codigo que permita mostrar todos los números primos que existan entre dos valores ingresados por el usuario, y muestre el total de números primos encontrados.'''

a=int(input('ingrese a:'))
b=int(input('ingrese b:'))
p=int(0)
e=int(0)
for c in range(a,b):
    for d in range(2,c-1):
        if(c%d==0):
            p+=1
    if(p==0):
        print('el numero',c,'que esta entre',a,'y',b,'es primo')
        e+=1
        p=int(0)
    else:
        p=int(0)
print('hay',e,'primos')
