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
Mostrar el empleado que mayor cantidad de horas extras haya realizado.
Hacer un excel con los datos pedidos al usuario'''

def excel():
    print('-'*117)
    print('|{0:10s}|{1:10s}|{2:8s}|{3:5s}|{4:9s}|{5:15s}|{6:7s}|{7:9s}|{8:18s}|{9:15s}|'.
        format('Nombre','Apellido','DNI','Edad','Area','Puesto','Sueldo','Horas Ex.','Cantidad Horas Ex','Año Ingreso'))
    print('-'*117)
    for i in range(len(vecaño)):
        print('|{0:10s}|{1:10s}|{2:8.0f}|{3:5.0f}|{4:9.0f}|{5:15s}|{6:7.0f}|{7:9.0f}|{8:18.0f}|{9:15.0f}|'.
            format(vecnoms[i],vecapes[i],vecdni[i],vecedades[i],vecareas[i],vecpuestos[i],vecsueldos[i],vechoras[i],veccant[i],vecaño[i]))
    print('-'*117)
    
def area(vec_are):
    while(vec_are[0]>3):
        vec_are=[]
        vec_are.append(int(input('ingrese un numero dependiendo el area de trabajo (1=Administracion, 2=Sistemas o 3=Logistica):')))
    return(vec_are[0])


def orden(vec_lista):
    for i in range(len(vec_lista)-1):
        for f in range(i+1,len(vec_lista)):
            if(vec_lista[i]>vec_lista[f]):
                aux=vec_lista[i]
                vec_lista[i]=vec_lista[f]
                vec_lista[f]=aux

def orden2():
    for i in range(len(vecaño)-1):
        for f in range(i+1,len(vecaño)):
            if(vecaño[i]>vecaño[f]):
                aux=vecaño[i]
                vecaño[i]=vecaño[f]
                vecaño[f]=aux
                aux=vecnoms[i]
                vecnoms[i]=vecnoms[f]
                vecnoms[f]=aux
                aux=vecapes[i]
                vecapes[i]=vecapes[f]
                vecapes[f]=aux
                aux=vecedades[i]
                vecedades[i]=vecedades[f]
                vecedades[f]=aux
                aux=vecsueldos[i]
                vecsueldos[i]=vecsueldos[f]
                vecsueldos[f]=aux
                aux=veccant[i]
                veccant[i]=veccant[f]
                veccant[f]=aux
                aux=vechoras[i]
                vechoras[i]=vechoras[f]
                vechoras[f]=aux
                aux=vecdni[i]
                vecdni[i]=vecdni[f]
                vecdni[f]=aux
    
def puesto(w):
    if(w==3):
        vec_pst.append(str(input('ingrese un puesto de trabajo (Deposito o Entregas):')).lower())
        vecpuestos.append(vec_pst)
    elif(w==2):
        vec_pst.append(str(input('ingrese un puesto de trabajo (Programadores 0 QA):')).lower())
        vecpuestos.append(vec_pst)
    else:
        vec_pst.append(str(input('ingrese un puesto de trabajo (Liquidaciones o Finanzas):')).lower())
        vecpuestos.append(vec_pst)

def datos_1():
    vec_nom.append(str(input('ingrese un nombre:')))
    vecnoms.append(vec_nom)
    vec_ape.append(str(input('ingrese un apellido:')))
    vecapes.append(vec_ape)
    vec_age.append(int(input('ingrese una edad:')))
    vecedades.append(vec_age)
    vec_are.append(int(input('ingrese un numero dependiendo el area de trabajo (1=Administracion, 2=Sistemas o 3=Logistica):')))
    vecareas.append(vec_are)
    vec_sld.append(int(input('ingrese un sueldo:')))
    vec_canth.append(int(input('ingrese la cantidad de horas extras:')))
    veccant.append(vec_canth)
    vec_valh.append(int(input('ingrese el valor de las horas extra:')))
    vec_dni.append(int(input('ingrese el numero de dni:')))
    vecdni.append(vec_dni)
    vec_aingr.append(int(input('ingrese el año de ingreso:')))
    vecaño.append(vec_aingr)

def hextra():
    aux=vec_canth[0]*vec_valh[0]
    print('el valor total por las horas extra es de',aux)

def sueldo_con_porc():
    aux=vec_sld[0]+vec_sld[0]/4
    vecsueldos.append(aux)
    print('al haber un aumento del %25 en el sueldo, el valor ahora es de',aux)
    
def hextra_con_porc():
    aux=vec_valh[0]+((vec_valh[0]*15)/100)
    vechoras.append(aux)
    print('al haber un aumento del %15 en las horas extra, el valor ahora es de',aux)
    aux*=vec_canth[0]
    print('el valor total de las horas extras ahora es de',aux)

vecnoms=[]
vecapes=[]
vecedades=[]
vecareas=[]
vecpuestos=[]
vecsueldos=[]
vechoras=[]
veccant=[]
vecdni=[]
vecaño=[]
vec3=['logistica']
vec2=['sistemas']
vec1=['administracion']
h=int(0)
j=int(0)
g=int(0)
k=int(0)
w=int(0)
vec_lista=[]
for c in range(10):

    vec_nom=[]
    vec_ape=[]
    vec_age=[]
    vec_are=[]
    vec_sld=[]
    vec_canth=[]
    vec_valh=[]
    vec_dni=[]
    vec_aingr=[]

    datos_1()
    
    vec_lista.append(vec_aingr[0])

    w+=area(vec_are)
    vec_pst=[]
    puesto(w)
    w=0
    
    hextra()
    
    sueldo_con_porc()

    hextra_con_porc()

    a=vec_sld[0]+vec_sld[0]/4
    if(a>h):
        h=a
        j=c+1
    if(vec_canth[0]>g):
        g=vec_canth[0]
        k=c+1
    

orden(vec_lista)
print('el sueldo mas alto fue el del empleado numero',j,'con un sueldo de',h)
print('el empleado que realizo mas horas extras fue el',k,'con',g,'horas extras')
print('el orden de los empleados segun su año de ingreso es',vec_lista)
orden2()
excel()
