#Manuel Ponce 3º 3º Grupo C

'''Se debe tener todo en funciones.
Un menú principal será el encargado de realizar el llamado a cada función, y las opciones de menú serán:

1) Alta de Empleado
2) Listado de Empleados
     1) Ordenado por DNI
     2) Ordenado por Apellido
     3) Ordenado por Sueldo Básico
     4) Ordenado por Cantidad de Horas Extras
     0) Volver
3) Aumento de Sueldo Básico General
4) Aumento del Valor Hora Extra
     1) por Área
     2) General
     0) Volver
5) Baja de Empleado
6) Modificaciòn de empleado
     1) por Área
     2) General
     0) Volver
0) Salir del Sistema.'''

def ingreso_opcion(op):
    a=int(0)
    op=int(-1)
    while(op!=0):
        op=int(input('Ingrese un número en base a esta lista\n 1° Alta de Empleados\n 2°Lista de empleados\n 3°Aumento Sueldo General\n 4°Aumento Valor de Horas Extra\n 5°Baja de Empleados\n 6° Modificar de Empleado\n 0° Salir\n Ingresar:'))
        if(op==1):
            a+=1
            datos_1()
        elif(op==2):
            us=int(5)
            while(us!=0):
                us=int(input('ingrese un número para ordenar en base a esta lista\n 1° DNI\n 2° Apellido\n 3° Sueldo Básico\n 4° Cantidad de horas extras\n 0° Volver\n Ingresar:'))
                if(us==1):
                    orden()
                elif(us==2):
                    orden2()
                elif(us==3):
                    orden3()
                elif(us==4):
                    orden4()
                elif(us==0):
                    print('volviendo...')
                else:
                    print('este número no se corresponde a ningúna accion')
        elif(op==3):
            sueldo_con_porc()
        elif(op==4):
            iz=int(3)
            while(iz!=0):
                iz=int(input('ingrese un número para definir que aumento aplicar en base a esta lista\n 1° Por Area\n 2° General\n 0° Volver\n Ingresar'))
                if(iz==1):
                    hextra_area()
                elif(iz==2):    
                    hextra_con_porc()
                elif(iz==0):
                    print('volviendo...')
                else:
                    print('este número no se corresponde a ningúna accion')
        elif(op==5):
            des_dato()
        elif(op==6):
            datos_2()
        elif(op==0):
            print('volviendo...')
        else:
            print('este número no se corresponde a ningúna accion')

def excel():
    print('-'*117)
    print('|{0:10s}|{1:10s}|{2:8s}|{3:5s}|{4:9s}|{5:15s}|{6:7s}|{7:9s}|{8:18s}|{9:15s}|'.
        format('Nombre','Apellido','DNI','Edad','Area','Puesto','Sueldo','Horas Ex.','Cantidad Horas Ex','Año Ingreso'))
    print('-'*117)
    for i in range(0,len(vec_aingr)):
        print('|{0:10s}|{1:10s}|{2:8.0f}|{3:5.0f}|{4:9.0f}|{5:15s}|{6:7.0f}|{7:9.0f}|{8:18.0f}|{9:15.0f}|'.
            format(vec_nom[i],vec_ape[i],vec_dni[i],vec_age[i],vec_are[i],vec_pst[i],vec_sld[i],vec_valh[i],vec_canth[i],vec_aingr[i]))
    print('-'*117)

def des_dato():
    buscar_dni=int(input('ingrese el numero de DNI del empleado a eliminar'))
    for i in range(len(vec_dni)):
        if(buscar_dni==vec_dni[i]):
            vec_dni.pop(i)
            vec_ape.pop(i)
            vec_age.pop(i)
            vec_are.pop(i)
            vec_sld.pop(i)
            vec_canth.pop(i)
            vec_valh.pop(i)
            vec_nom.pop(i)
            vec_aingr.pop(i)
            vec_pst.pop(i)
            break

def datos_1():
    w=int(0)
    vec_nom.append(str(input('ingrese un nombre:')))
    vec_ape.append(str(input('ingrese un apellido:')))
    vec_age.append(int(input('ingrese una edad:')))
    vec_are.append(int(input('ingrese un numero dependiendo el area de trabajo (1=Administracion, 2=Sistemas o 3=Logistica):')))
    w+=area()
    vec_sld.append(int(input('ingrese un sueldo:')))
    vec_canth.append(int(input('ingrese la cantidad de horas extras:')))
    vec_valh.append(int(input('ingrese el valor de las horas extra:')))
    vec_dni.append(int(input('ingrese el numero de dni:')))
    vec_aingr.append(int(input('ingrese el año de ingreso:')))
    puesto(w)
    w=0

def datos_2():
    w=int(0)
    if(len(vec_nom)!=0):
        vec_nom[len(vec_nom)-1]=(str(input('ingrese un nombre:')))
        vec_ape[len(vec_nom)-1]=(str(input('ingrese un apellido:')))
        vec_age[len(vec_nom)-1]=(int(input('ingrese una edad:')))
        vec_are[len(vec_nom)-1]=(int(input('ingrese un numero dependiendo el area de trabajo (1=Administracion, 2=Sistemas o 3=Logistica):')))
        w+=area2()
        vec_sld[len(vec_nom)-1]=(int(input('ingrese un sueldo:')))
        vec_canth[len(vec_nom)-1]=(int(input('ingrese la cantidad de horas extras:')))
        vec_valh[len(vec_nom)-1]=(int(input('ingrese el valor de las horas extra:')))
        vec_dni[len(vec_nom)-1]=(int(input('ingrese el numero de dni:')))
        vec_aingr[len(vec_nom)-1]=(int(input('ingrese el año de ingreso:')))
        puesto2(w)
        w=0


def area2():
    if(len(vec_nom)!=0):
        aux=vec_are[len(vec_nom)-1]
        while(aux>3):
            vec_are[len(vec_nom)-1]=[]
            vec_are[len(vec_nom)-1]=(int(input('ingrese un numero dependiendo el area de trabajo (1=Administracion, 2=Sistemas o 3=Logistica):')))
            aux=vec_are[len(vec_nom)-1]
        return(aux)

def area():
        aux=vec_are[len(vec_nom)-1]
        while(aux>3):
            vec_are[len(vec_nom)-1]=[]
            vec_are[len(vec_nom)-1]=(int(input('ingrese un numero dependiendo el area de trabajo (1=Administracion, 2=Sistemas o 3=Logistica):')))
            aux=vec_are[len(vec_nom)-1]
        return(aux)

def puesto(w):
    if(w==3):
        vec_pst.append(str(input('ingrese un puesto de trabajo (Deposito o Entregas):')).lower())
    elif(w==2):
        vec_pst.append(str(input('ingrese un puesto de trabajo (Programadores 0 QA):')).lower())
    else:
        vec_pst.append(str(input('ingrese un puesto de trabajo (Liquidaciones o Finanzas):')).lower())

def puesto2(w):
    if(len(vec_nom)!=0):
        if(w==3):
            vec_pst[len(vec_nom)-1]=(str(input('ingrese un puesto de trabajo (Deposito o Entregas):')).lower())
        elif(w==2):
            vec_pst[len(vec_nom)-1]=(str(input('ingrese un puesto de trabajo (Programadores 0 QA):')).lower())
        else:
            vec_pst[len(vec_nom)-1]=(str(input('ingrese un puesto de trabajo (Liquidaciones o Finanzas):')).lower())

def orden():
    for i in range(len(vec_dni)-1):
        for f in range(i+1,len(vec_dni)):
            if(vec_dni[i]>vec_dni[f]):
                aux=vec_dni[i]
                vec_dni[i]=vec_dni[f]
                vec_dni[f]=aux
                aux=vec_nom[i]
                vec_nom[i]=vec_nom[f]
                vec_nom[f]=aux
                aux=vec_ape[i]
                vec_ape[i]=vec_ape[f]
                vec_ape[f]=aux
                aux=vec_age[i]
                vec_age[i]=vec_age[f]
                vec_age[f]=aux
                aux=vec_sld[i]
                vec_sld[i]=vec_sld[f]
                vec_sld[f]=aux
                aux=vec_canth[i]
                vec_canth[i]=vec_canth[f]
                vec_canth[f]=aux
                aux=vec_valh[i]
                vec_valh[i]=vec_valh[f]
                vec_valh[f]=aux
                aux=vec_aingr[i]
                vec_aingr[i]=vec_aingr[f]
                vec_aingr[f]=aux
    excel()

def orden2():
    for i in range(len(vec_ape)-1):
        for f in range(i+1,len(vec_ape)):
            if(vec_ape[i]>vec_ape[f]):
                aux=vec_ape[i]
                vec_ape[i]=vec_ape[f]
                vec_ape[f]=aux
                aux=vec_nom[i]
                vec_nom[i]=vec_nom[f]
                vec_nom[f]=aux
                aux=vec_dni[i]
                vec_dni[i]=vec_dni[f]
                vec_dni[f]=aux
                aux=vec_age[i]
                vec_age[i]=vec_age[f]
                vec_age[f]=aux
                aux=vec_sld[i]
                vec_sld[i]=vec_sld[f]
                vec_sld[f]=aux
                aux=vec_canth[i]
                vec_canth[i]=vec_canth[f]
                vec_canth[f]=aux
                aux=vec_valh[i]
                vec_valh[i]=vec_valh[f]
                vec_valh[f]=aux
                aux=vec_aingr[i]
                vec_aingr[i]=vec_aingr[f]
                vec_aingr[f]=aux
    excel()

def orden3():
    for i in range(len(vec_sld)-1):
        for f in range(i+1,len(vec_sld)):
            if(vec_sld[i]>vec_sld[f]):
                aux=vec_sld[i]
                vec_sld[i]=vec_sld[f]
                vec_sld[f]=aux
                aux=vec_nom[i]
                vec_nom[i]=vec_nom[f]
                vec_nom[f]=aux
                aux=vec_dni[i]
                vec_dni[i]=vec_dni[f]
                vec_dni[f]=aux
                aux=vec_age[i]
                vec_age[i]=vec_age[f]
                vec_age[f]=aux
                aux=vec_ape[i]
                vec_ape[i]=vec_ape[f]
                vec_ape[f]=aux
                aux=vec_canth[i]
                vec_canth[i]=vec_canth[f]
                vec_canth[f]=aux
                aux=vec_valh[i]
                vec_valh[i]=vec_valh[f]
                vec_valh[f]=aux
                aux=vec_aingr[i]
                vec_aingr[i]=vec_aingr[f]
                vec_aingr[f]=aux
    excel()
                    
def orden4():
    for i in range(len(vec_canth)-1):
        for f in range(i+1,len(vec_canth)):
            if(vec_canth[i]>vec_canth[f]):
                aux=vec_canth[i]
                vec_canth[i]=vec_canth[f]
                vec_canth[f]=aux
                aux=vec_nom[i]
                vec_nom[i]=vec_nom[f]
                vec_nom[f]=aux
                aux=vec_dni[i]
                vec_dni[i]=vec_dni[f]
                vec_dni[f]=aux
                aux=vec_age[i]
                vec_age[i]=vec_age[f]
                vec_age[f]=aux
                aux=vec_ape[i]
                vec_ape[i]=vec_ape[f]
                vec_ape[f]=aux
                aux=vec_sld[i]
                vec_sld[i]=vec_sld[f]
                vec_sld[f]=aux
                aux=vec_valh[i]
                vec_valh[i]=vec_valh[f]
                vec_valh[f]=aux
                aux=vec_aingr[i]
                vec_aingr[i]=vec_aingr[f]
                vec_aingr[f]=aux 
    excel()

def sueldo_con_porc():
    juanchito=int(input('ingrese el porcentaje de aumento del sueldo basico general sin el %:'))
    for j in range(len(vec_sld)):
        vec_sld[j]=(vec_sld[j]*juanchito)/100
    print('se aumento en un',juanchito,'por ciento el sueldo basico general')
        
def hextra_con_porc():
    juancho=int(input('ingrese el porcentaje de aumento de las horas extra sin el %:'))
    for j in range(len(vec_valh)):
        aux=vec_valh[j]
        vec_valh[j]=(vec_valh[j]*juancho)/100
    print('se aumento en un',juancho,'por ciento el valor de las horas extra')

def hextra_area():
    aux=int(input('ingrese el número del area la cual quiera darle un aumento\n 1° Administracion\n 2° Sistema\n 3° Logistica'))
    areaux(aux)
    ec=int(input('ingrese el porcentaje de aumento de las horas extra sin el %:'))
    for p in range(len(vec_are)):
        if(aux==vec_are[p]):
            vec_are[p]=(vec_are[p]*ec)/100
    print('se aumento en un',ec,'por ciento el valor de las horas extras en el area',aux)

def areaux(aux):
    while(aux>=4 or aux <=0):
        aux=int(input('ingrese el número del area la cual quiera darle un aumento\n 1° Administracion\n 2° Sistema\n 3° Logistica'))
    return(aux)

op=int(-69)
vec_nom=[]
vec_ape=[]
vec_age=[]
vec_are=[]
vec_sld=[]
vec_canth=[]
vec_valh=[]
vec_dni=[]
vec_aingr=[]
vec_pst=[]
ingreso_opcion(op)
print('fin')
