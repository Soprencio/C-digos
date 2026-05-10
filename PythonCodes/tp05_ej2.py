#Manuel Ponce 3º 3º Grupo C

'''Hacer un programa que permita encontrar los primeros 4 números perfectos, teniendo en cuenta que se denomina número perfecto a aquellos números donde la suma de sus
divisores, menos si mismo, da el mismo número.Implementar una función es_perfecto(n) que devuelva si es o no perfecto.'''

def es_perfecto(n):
    b=int(0)
    for c in range(1,n):
        if(n%c==0):
            b+=c
    if(n==b):
        return(True)
    else:
        return(False)

n=int(1)
t=int(0)
while(t<4):
    if(es_perfecto(n)):
        print(n,end=',')
        t+=1
    n+=1
print("\nHay",t,"numeros perfectos")
        

    
