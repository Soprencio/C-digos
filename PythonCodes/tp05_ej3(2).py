def es_amigo(a,b):
    d=int(0)
    e=int(0)
    for c in range(1,a-1):
        if(a%c==0):
            d+=c
    for c in range(1,b-1):
        if(b%c==0):
            e+=c
    if(a==e):
        if(b==d):
            return(True)
    return(False)

a=int(input('ingrese a:'))
b=int(input('ingrese b:'))
if(es_amigo(a,b)):
    print(a,'y',b,'son amigos')
else:
    print(a,'y',b,'no son amigos')
