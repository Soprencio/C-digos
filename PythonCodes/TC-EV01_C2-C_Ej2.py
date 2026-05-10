#Manuel Ponce 3° 3° Grupo C

''' A) Modificar la definición de mat para que tenga 4 filas por 4
columnas utilizando una función crea_matriz(f, c).

    B) Escribir la función carga_matriz(p, m, f, c), que debe
agregarse al código luego de que la matriz esté creada, y se
encargará de distribuir una palabra de 16 caracteres en forma
de zig-zag.'''

def crea_matriz(f,c):
    mat=[None]*f
    for i in range(f):
        mat[i]=[None]*c
    return(mat)

def carga_matriz(p,m,f,c):
    print(p)
    aux=int(0)
    booliano=int(1)
    for i in range(f):
        if(booliano==0):
            for j in range(c-1,-1,-1):
                m[i][j]=p[aux]
                aux+=1
            booliano=1
        elif(booliano==1):
            for j in range(c):
                m[i][j]=p[aux]
                aux+=1
            booliano=0

def mostrar():
    for i in range(f):
        for j in range(c):
            print(m[i][j],end=' ')
        print()

#Columnas
c=int(4)

#Filas
f=int(4)

#Palabra
p=input('Ingrese una palabra de 16 caracteres (Ej constitucionales): ')
while(len(p)!=16):
    p=input('Esa palabra no tiene 16 caracteres: ')

m=crea_matriz(f,c)
carga_matriz(p,m,f,c)
mostrar()
