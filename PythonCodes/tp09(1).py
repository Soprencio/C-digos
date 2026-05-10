#Manuel Ponce 3° 3° Grupo C

'''Una empresa necesita almacenar los datos de sus diez empleados, donde los datos relevantes son:

          [DNI, APELLIDO, Nombre, Puesto, Área, Año_Ingreso, Sueldo_Básico, Horas_Extras, Valor_Horas_Extras]
Los empleados están en diferentes áreas

                        [Administración, Sistemas, Logística]

y los puestos que ocupan son

                        [Liquidaciones, Finanzas, Programadores, QA, Depósito, Entregas]

y están relacionados cada dos puestos por área.

Se pide:
Aumentar el sueldo básico de todos los empleados de la empresa en un 25%.
Aumentar el valor de horas extras de los empleados de Sistemas en 15%
Ordenar la lista de empleados según el Año_Ingreso.
Mostrar el sueldo final más alto.
Mostrar el empleado que mayor cantidad de horas extras haya realizado.'''

def area(vec_are):
    while(vec_are[0]>3):
        vec_are=[]
        vec_are.append(int(input('ingrese un numero dependiendo el area de trabajo (1=Administracion, 2=Sistemas o 3=Logistica):')))


def orden(vec_lista):
    for i in range(len(vec_lista)-1):
        for f in range(i+1,len(vec_lista)):
            if(vec_lista[i]>vec_lista[f]):
                aux=vec_lista[i]
                vec_lista[i]=vec_lista[f]
                vec_lista[f]=aux
		

vec3=['logistica']
vec2=['sistemas']
vec1=['administracion']
h=int(0)
j=int(0)
g=int(0)
k=int(0)
vec_lista=[]
for c in range(10):
    aux=int(0)
    a=int(0)
    b=int(0)
    vec_nom=[]
    vec_nom.append(str(input('ingrese un nombre:')))
    vec_ape=[]
    vec_ape.append(str(input('ingrese un apellido:')))
    vec_age=[]
    vec_age.append(int(input('ingrese una edad:')))
    vec_are=[]
    vec_are.append(int(input('ingrese un numero dependiendo el area de trabajo (1=Administracion, 2=Sistemas o 3=Logistica):')))
    vec_pst=[]

    area(vec_are)
    
    if(vec_are[0]==3):
        vec_pst.append(str(input('ingrese un puesto de trabajo (Deposito o Entregas):')).lower())
    elif(vec_are[0]==2):
        vec_pst.append(str(input('ingrese un puesto de trabajo (Programadores 0 QA):')).lower())
    else:
        vec_pst.append(str(input('ingrese un puesto de trabajo (Liquidaciones o Finanzas):')).lower())
        
    vec_sld=[]
    vec_sld.append(int(input('ingrese un sueldo:')))
    vec_canth=[]
    vec_canth.append(int(input('ingrese la cantidad de horas extras:')))
    vec_valh=[]
    vec_valh.append(int(input('ingrese el valor de las horas extra:')))
    vec_dni=[]
    vec_dni.append(int(input('ingrese el numero de dni:')))
    vec_aingr=[]
    vec_aingr.append(int(input('ingrese el año de ingreso:')))
    vec_lista.append(vec_aingr[0])
    a=vec_canth[0]
    b=vec_valh[0]
    aux=a*b
    print('el valor total por las horas extra es de',aux)
    a=vec_sld[0]+vec_sld[0]/4
    print('al haber un aumento del %25 en el sueldo, el valor ahora es de',a)
    if(a>h):
        h=a
        j=c+1
    b=vec_valh[0]+((vec_valh[0]*15)/100)
    if(vec_canth[0]>g):
        g=vec_canth[0]
        k=c+1
    print('al haber un aumento del %15 en las horas extra, el valor ahora es de',b)
    b*=vec_canth[0]
    print('el valor total de las horas extras ahora es de',b)
    
orden(vec_lista)
print('el sueldo mas alto fue el del empleado numero',j,'con un sueldo de',h)
print('el empleado que realizo mas horas extras fue el',k,'con',g,'horas extras')
print('el orden de los empleados segun su año de ingreso es',vec_lista)
