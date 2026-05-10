vece=[]
vecf=[]
vecg=[]
vech=[]
veci=[]
vecj=[]
for c in range(1,5):
    print('ingrese los valores de los productos del vendedor',c)
    prod1=int(input('ingresar el valor del producto 1:')) 
    prod2=int(input('ingresar el valor del producto 2:'))
    prod3=int(input('ingresar el valor del producto 3:'))
    prod4=int(input('ingresar el valor del producto 4:'))
    prod5=int(input('ingresar el valor del producto 5:'))
    prod6=int(input('ingresar el valor del producto 6:'))

    print('ingrese los descuentes correspondientes (colocando el numero sin %) de cada producto del vendedor',c)
    desc1=int(input('ingresar el descuento del producto 1:'))
    desc2=int(input('ingresar el descuento del producto 2:'))
    desc3=int(input('ingresar el descuento del producto 3:'))
    desc4=int(input('ingresar el descuento del producto 4:'))
    desc5=int(input('ingresar el descuento del producto 5:'))
    desc6=int(input('ingresar el descuento del producto 6:'))

    prod1-=(prod1*desc1)/100
    prod2-=(prod2*desc2)/100
    prod3-=(prod3*desc3)/100
    prod4-=(prod4*desc4)/100
    prod5-=(prod5*desc5)/100
    prod6-=(prod6*desc6)/100

    print('estos son los precios desde el producto 1 hasta el 6 con el descuento aplicado:\n',prod1,'\n',prod2,'\n',prod3,'\n',prod4,'\n',prod5,'\n',prod6)
    if(c==1):
        vece.append(prod1)
        vecf.append(prod2)
        vecg.append(prod3)
        vech.append(prod4)
        veci.append(prod5)
        vecj.append(prod6)
        vece.append(1)
        vecf.append(1)
        vecg.append(1)
        vech.append(1)
        veci.append(1)
        vecj.append(1)
    else:
        if(prod1<vece[0]):
            vece[0]=prod1
            vece[1]=c
        if(prod2<vecf[0]):
            vecf[0]=prod2
            vecf[1]=c
        if(prod3<vecg[0]):
            vecg[0]=prod3
            vecg[1]=c
        if(prod4<vech[0]):
            vech[0]=prod4
            vech[1]=c
        if(prod5<veci[0]):
            veci[0]=prod5
            veci[1]=c
        if(prod6<vecj[0]):
            vecj[0]=prod6
            vecj[1]=C
print('el vendedor con el producto 1 mas barato es el número',vece[1],'con un precio de',vece[0])
print('el vendedor con el producto 2 mas barato es el número',vecf[1],'con un precio de',vecf[0])
print('el vendedor con el producto 3 mas barato es el número',vecg[1],'con un precio de',vecg[0])
print('el vendedor con el producto 4 mas barato es el número',vech[1],'con un precio de',vech[0])
print('el vendedor con el producto 5 mas barato es el número',veci[1],'con un precio de',veci[0])
print('el vendedor con el producto 6 mas barato es el número',vecj[1],'con un precio de',vecj[0])
