#Ponce Manuel 3º 3º Grupo C

'''Hacer un codigo que permita ingresar dos valores numéricos enteros y resuelva la potencia entre ambos y mostrar el resultado.'''


a=int(input('ingrese a:'))
b=int(input('ingrese b:'))
p=int(1)
for c in range(0,b):
    p*=a
print(a,'elevado',b,'es:',p)
