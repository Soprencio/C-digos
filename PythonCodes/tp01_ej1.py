#Ponce Manuel 3º 3º Grupo C

'''Hacer el codigo de flujo para un programa que permita ingresar dos valores enteros, y realice las cuatro operaciones aritméticas básicas (+, -, *, /) y muestre sus
correspondientes resultados. Se pide validar el caso de la división por cero.'''

p=float(0.0)
j=float(0.0)
z=float(0.0)
x=float(0.0)
a=int(input('ingrese a:'))
b=int(input('ingrese b:'))
p=a+b
print(a,'mas',b,'es:',p)
j=a-b
print(a,'menos',b,'es:',j)
x=a*b
print(a,'multiplicado',b,'es:',x)
if(b==0):
    print(a,'divido 0 no tiene resultado en números reales')
else:
    z=a/b
    print(a,'dividido',b,'es:',z)
