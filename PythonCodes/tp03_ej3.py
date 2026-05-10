#Ponce Manuel 3º 3º Grupo C

'''Hacer un codigo que permita el ingreso del apellido y nombre de cinco alumnos, para cada alumno, permita el ingreso del nombre de materia y tres notas para cinco materias,
que calcule el promedio de cada materia y muestre el promedio de cada materia.'''

p=int(0)
for c in range(1,6): #la no condicional va hasta 6 porque si ponemos 5, ira contando 1,2,3 y 4 pero sin llegar y pasar por el cinco, teniendo solo 4 repeticiones
    a=input('ingrese el nombre del alumno:')
    b=input('ingrese el apellido del alumno:')
    for d in range(1,6): #la misma razón que con el "for in range" anterior
        e=input('ingrese el nombre de una materia:')
        f=int(input('ingrese la nota 1:'))
        g=int(input('ingrese la nota 2:'))
        h=int(input('ingrese la nota 3:'))
        p=(f+g+h)/3
        print('el promedio entre las 3 notas de la materia',e,'del alumno',a,b,'es de:',p)
        
