#Manuel Ponce 3° 3° Grupo C

'''Hacer un programa que permita crear un vector de 20 elementos y llene el vector con valores enteros generados al azar, de manera que los valores se almacenan siempre un valor
impar luego de un valor par, y además se vayan generando ordenados de menor a mayor.'''

import random
vec=[None]*20
for i in range(1,21):
    vec[i-1]=random.randint(1,i*i*i+8)
    if(i>1):
        if(i%2==0):
            while(vec[i-1]%2!=0 or vec[i-1]<=vec[i-2]):
                vec[i-1]=random.randint(1,i*i*i+8)
        else:
            while(vec[i-1]%2!=1  or vec[i-1]<=vec[i-2]):
                vec[i-1]=random.randint(1,i*i*i+8)
    else:
        if(i%2==0):
            while(vec[i-1]%2!=0):
                vec[i-1]=random.randint(1,i*i*i+8)
        else:
            while(vec[i-1]%2!=1):
                vec[i-1]=random.randint(1,i*i*i+8)
print(vec)
