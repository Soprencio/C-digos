x=int(0)
w=''
z=int(0)
y=''
mb=int(0)
mv=int(0)
for c in range(1,6):
    a=input('ingrese el nombre de un alumno:')
    f=int(0)
    g=int(0)
    h=int(0)
    for d in range(1,5):
        bimestre=int(0)
        b=int(input('\ningrese la nota de la materia uno:'))
        e=int(input('ingrese la nota de la materia dos:'))
        bimestre=(b+e)/2
        if(b>=6):
            print('\n',a,'aprobo la materia uno del bimestre',d)
        else:
            print('\n',a,'reprobo la materia uno del bimestre',d)
        if(e>=6):
            print(a,'aprobo la materia dos del bimestre',d)
        else:
            print(a,'reprobo la materia dos del bimestre',d)
        if(bimestre>=6):
            print(a,'aprobo el bimestre',d,'con una nota de',bimestre)
        else:
            print(a,'reprobo el bimestre',d,'con una nota de',bimestre)
        f+=bimestre
        g+=b
        h+=e
    f/=4
    if(f>=6):
        print('\nla nota final del alumno',a,'es de',f,'y aprobo el año\n')
    else:
        print('\nla nota final del alumno',a,'es de',f,'y reprobo el año\n')
    g/=4
    if(g>=6):
        print('la nota final de la materia uno del alumno',a,'es de',g,'y aprobo la materia\n')
    else:
        print('la nota final de la materia uno del alumno',a,'es de',g,'y reprobo la materia\n')
    h/=4
    if(h>=6):
        print('la nota final de la materia dos del alumno',a,'es de',h,'y aprobo la materia\n')
    else:
        print('la nota final de la materia dos del alumno',a,'es de',h,'y reprobo la materia\n')
    if(g>x):
        x=g
        w=a
    if(h>z):
        z=h
        y=a  
    
print('\nla mejor nota final de la materia uno fue la de',w,'con una nota de',x)
print('\nla mejor nota final de la materia dos fue la de',y,'con una nota de',z)

       
        
