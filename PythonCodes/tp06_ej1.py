def buscar_letra(a):
    len(a)
    c=int(0)
    for i in range(len(a)):
        if(a[i]==b):
            print('la letra',b,'se encuentra en la posicion',i)
            c+=1
    return(c)

a=input('ingrese una cadena de caracteres:')
b=input('ingrese la letra a buscar:')
e=int(0)
e=buscar_letra(a)
if(e==0):
    print('en la cadena',a,'no hay ninguna letra',b)
else:
    print('hay',e,'letras',b,'en la cadena',a)
        
