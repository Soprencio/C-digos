import random
def cargar_vector(a,b,vec,j):
    for i in range(15):
        vec[i]=random.randint(a,b)
        while(vec[i]%2!=j):
            vec[i]=random.randint(a,b)

def mostrar_vec():
    print(vec1,vec2)

def ordenar_vec():
    for i in range(len(vec1)-1):
        for j in range(i+1,len(vec1)):
            if(vec1[i]<vec1[j]):
                aux=vec1[i]
                vec1[i]=vec1[j]
                vec1[j]=aux
    for i in range(len(vec2)-1):
        for j in range(i+1,len(vec2)):
            if(vec2[i]<vec2[j]):
                aux=vec2[i]
                vec2[i]=vec2[j]
                vec2[j]=aux

def intercalar_vec():
    o=int(0)
    for c in range(29):
        if(c%2==0):
            vec3[c]=vec1[o]
            vec3[c+1]=vec2[o]
            o+=1
    print(vec3)

a=int(input('ingrese desde que numero se generaran los valores:'))
b=int(input('ingrese hasta que numero se generaran los valores:'))
vec1=[None]*15
vec2=[None]*15
vec3=[None]*30
j=int(1)
cargar_vector(a,b,vec1,j)
j=int(0)
cargar_vector(a,b,vec2,j)
mostrar_vec()
ordenar_vec()
mostrar_vec()
intercalar_vec()
