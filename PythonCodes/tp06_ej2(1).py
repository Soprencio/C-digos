#Manuel Ponce 3º 3º Grupo C

'''Hacer un programa que permita el ingreso de una palabra o frase y verifique que la misma es o no palíndroma utilizando una función es_palindroma(<cadena>). En caso de no
ser palíndroma, verificar si la misma es palíndroma pero sacando los espacios de la cadena, si los tuviera, implementando una función sacar_espacios(<cadena>). De continuar
siendo no palíndroma, entonces, convertirla en palíndroma de la forma más corta posible utilizando una nueva función convertir_palindroma(<cadena>) que devolverá la cadena
convertida.'''

def convertir_palindromo(a):
    k=a
    g=a
    w=int(0)
    while(es_palindromo(a)==False):
        k=g
        k+=a[w::-1]
        w+=1
        a=k
    return(k)
        
def es_palindromo(a):
    b=int(0)
    len(a)
    for i in range(len(a)//2):
        if(a[i]==a[(len(a)-1)-i]):
                b+=1
    if(b==len(a)//2):
        return(True)
    else:
        return(False)

def sacar_espacios(a):
    len(a)
    h=''
    for i in range(0,len(a)):
        if(a[i]!=' '):
            h+=a[i]
    if(es_palindromo(h)):
        return(True)
    return(False)
    

a=input('ingrese una cadena de caracteres:').lower()
if(es_palindromo(a)):
    print(a,'es palindromo')
else:
    print(a,'no es palindromo')
    if(sacar_espacios(a)):
        print(a,'seria un palindromo si no tuviera espacios')
    else:
        print(a,'tampoco seria un palindromo si no tuviera espacios')
        print(a,'seria palindromo si fuera',convertir_palindromo(a))
