
def base_2(a):
    d=int(0)
    e='0'
    f='1'
    d=a
    b=''
    while(d>=2):
        if(d%2==0):
            b+=e
        else:
            b+=f
        d//=2
    b+=f
    b=b[::-1]
    return(b)

a=int(input('ingrese un numero:'))
print(a,'en base 2 se escribe',base_2(a))
