#Ponce Manuel 3º 3º Grupo C

'''Hacer un codigo para mostrar los números pares e impares desde un valor inicial hasta un valor final.'''

a=int(input('ingrese a:'))
b=int(input('ingrese b:'))
print('aqui tiene una lista de los números pares e impares entre',a,'y',b)
for c in range(a+1,b): #la razón de colocar a+1 es para que no muestre si A es par o impar, solo los números entre A y B
    if(c%2==0):
        print(c,'es par')
    else:
        print(c,'es impar')
