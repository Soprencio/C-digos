#Manuel Ponce 3° 3° Grupo C

'''Realizar el código en Python que permita resolver el siguiente
problema:
Se desea realizar la compra de 6 productos que son provistos
por 4 proveedores distintos, de los cuales se conoce el precio
de compra y el porcentaje de descuento que ofrece el
proveedor.
Se debe calcular el precio final de compra de cada producto y
cada proveedor indicando el menor costo para cada producto.
Realizar una aplicación Tkinter donde se puedan ingresar los
valores y mostrar los resultados.'''

from tkinter import *
from tkinter import messagebox
from functools import partial

def pre_comienzo():
    caja.configure(state='normal')
    caja.delete('1.0',END)
    caja.configure(state='disable')
    vec_prov[0]=1
    comienzo(vec_prov)

def comienzo(vec_prov):
    top=Toplevel()
    top.geometry('400x200+600+100')
    top.title('Proveedor N° '+str(vec_prov[0]))

#Advertencia para que no cierres y pierdas lo que ya se escribió
    top.protocol('WM_DELETE_WINDOW',partial(confirma,top,vec_prov))
    
    datos(top,vec_prov)

def confirma(top,vec_prov):
    if(confirmante[0]==0):
        confirmante[0]=1
        messagebox.showinfo(title='Advertencia',message='Si aprietas otra ves, se perderan los datos puestos')
    else:
        confirmante[0]=0
        top.destroy()
        caja.configure(state='normal')
        caja.delete('1.0',END)
        caja.configure(state='disable')
        vec_prov[0]=1

def datos(top,vec_prov):
#Reinicia los vectores para reutilizarlos a lo largo de los Toplevel
    for i in range(len(texto)):
        texto.pop()
    for i in range(len(entry)):
        entry.pop()

#Coloca en el Toplevel los entry y label
    for c in range(7):
        if(c<6):
            texto.append(Label(top,text='Precio'+str(c+1)+': '))
        else:
            texto.append(Label(top,text='Descuento(sin %): '))
        entry.append(Entry(top))
    for c in range(7):
        texto[c].grid(row=c,column=0)
        entry[c].grid(row=c,column=1)
    agre=Button(top,text='Agregar',command=partial(agregar,top,vec_prov))
    agre.place(x=330,y=160,height=30,width=60)

def agregar(top,vec_prov):
    aux2=int(0)
    for c in range(7):
        if(len(entry[c].get())<1):
            aux2+=1
    if(aux2<1):
        if(int(entry[6].get())<100 and int(entry[6].get())>0):
        #Inserta en el Text de 'ventana' los precios, el descuento y el correspondiente proveedor
            caja.configure(state='normal')
            caja.insert(END,'\nProveedor'+str(vec_prov[0])+'\n')
            for c in range(7):
                if(c<6):
                    caja.insert(END,entry[c].get()+'\n')
                else:
                    caja.insert(END,'%'+entry[c].get()+'\n')

        #Inserta en el Text de 'ventana' los precios con su respectivo descuento
            aux=int(entry[6].get())
            caja.insert(END,'Aqui tiene los precios con el descuento:\n')
            for c in range(6):
                desc=int(entry[c].get())-((int(entry[c].get()))*aux)/100
                caja.insert(END,str(desc)+'\n')
                producto_barato[c]=desc

        #Coloca los datos originales para que no compare con 0 (siempre se quedaria el 0)
            if(vec_prov[0]==1):
                for i in range(6):
                    producto_baratisimo[i]=producto_barato[i]+1

        #Compara los precios de los producots (Alojados en p_barato) con los precios anterios (Alojados en p_baratisimo) y guarda en este último los precios solo si el nuevo es más barato
            for i in range(6):
                if(producto_barato[i]<producto_baratisimo[i]):
                    producto_baratisimo[i]=producto_barato[i]
                    provee[i]=vec_prov[0]
            top.destroy()
            vec_prov[0]+=1

        #Corrobora que se hagan solo 4 proveedores
            if(vec_prov[0]<5):
                comienzo(vec_prov)
            else:
                
        #Termina el código enseñando en el Text el precio mas barato de cada producto junto al proveedor que lo vende
                caja.insert(END,'\n')
                messagebox.showinfo(title='Listo',message='Ya has puesto a todos los proveedores, mira los precios mas bajos por producto')
                for c in range(6):
                    caja.insert(END,'producto '+str(c+1)+': \n'+str(producto_baratisimo[c])+' del proveedor '+str(provee[c])+'\n \n')
                
            caja.configure(state='disable')
        else:
            messagebox.showinfo(title='Error',message='El porcentaje de descuenta debe oscilar entre 1 y 99')
    else:
        messagebox.showinfo(title='Error',message='Debes colocar algun valor numerico entero dentro de los espacios para escribir')
    
ventana= Tk()
ventana.geometry('575x900+100+100')
ventana.title('Proveedores - Productos')

#Vectores que contienen los entrys y labels de los Toplevel, los precios mas bajos para comparar y el num de proveedor
vec_prov=[1]
producto_barato=[0,0,0,0,0,0]
producto_baratisimo=[0,0,0,0,0,0]
provee=[0,0,0,0,0,0]
texto=[]
entry=[]

#Obliga a apretar dos veces la X para cerrar Toplevel y no perder la información por descuido
confirmante=[0]

comenzar=Button(ventana,text='Comenzar',command=pre_comienzo)
comenzar.place(x=240,y=70,height=30,width=80)

caja=Text(ventana,state='disable')
caja.place(x=100,y=120,height=750,width=350)

ventana.mainloop()
