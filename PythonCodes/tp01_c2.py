#Manuel Ponce 3° 3° Grupo C

'''Tomando como base el ejercicio de Buenos-Malos-Regulares del TC-TP07-C1 que decía:

Manejo de Cadenas de Caracteres

Hacer un programa que permita generar de un número de cuatro dígitos distintos entre si y los almacene en una cadena de caracteres. Ese número generado será el número que tendremos que adivinar.

El programa deberá solicitar al usuario que ingrese un número de hasta cuatro dígitos y deberá devolver la información sobre los números ingresados y su estado. '''

import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def parecidos():
    e=int(0)
    f=int(0)
    g=int(0)
    aux=''
    for c in range(4):
        j=int(0)
        while(a[0][c]!=b[0][j]and j<3):
            j+=1
        if(a[0][c]==b[0][j]):
            if(c==j):
                e+=1
            else:
                f+=1
        else:
            g+=1
    
    return(aux+str(e)+'B'+str(f)+'R'+str(g)+'M\n')

def numero_esta(x,n):
    for i in range(len(x)):
        if(str(n)==x[i]):
            return(True)
    return(False)
    
def generar_num():
    p[0]=0
    caja_texto.delete('1.0',END)
    x=''
    for c in range(4):
        n=random.randint(0,9)
        while(numero_esta(x,n)):
              n=random.randint(0,9)
        x+=str(n)
    b[0]=x
    k[0]=1

def numero_esta2():
    for i in range(len(a[0])-1):
        for j in range(i+1,len(a[0])):
            if(a[0][i]==a[0][j]):
                messagebox.showinfo(title='Error',message='No puedes ingresar un número con digitos repetidos')
                return(False)
    return(True)

def numero_es4():
    if(len(a[0])==4):
        return(True)
    else:
        messagebox.showinfo(title='Error',message='Tu número debe ser de 4 caracteres, ni uno más ni no menos')
        return(False)

def numerico():
    h=int(0)
    for i in range(10000):
        f=str(a[0])
        y=str(i)
        if(f==y):
            h+=1
    if(h<1):
        messagebox.showinfo(title='Error',message='El numero ingreso contiene caracteres no numericos')
        return(False)
    return(True)

def jugar():
    if(k[0]==1):
        aux2='4B0R0M\n'
        a[0]=entry.get()
        if(numero_esta2() and numero_es4() and numerico()):
            caja_texto.insert(END,parecidos())
            if(parecidos()==aux2):
                messagebox.showinfo(title='Felicitaciones',message='Has adivinado el numero '+b[0])
                ven.destroy()
            entry.delete(0,END)
            entry.focus()
            p[0]+=1
            if(p[0]==10):
                messagebox.showinfo(title='Que mal...',message='Has perdido, el numero era '+b[0])
                ven.destroy()
    else:
        messagebox.showinfo(title='Error',message='Todavia no se ha generado un número')

k=[0]
p=[0]
a=[None]*1
b=[None]*1
ven=Tk()
ven.geometry('400x350')
ven.title('buenos, malos y regulares')
bot=Button(text='Genera Número',command=generar_num)
entry=Entry(width=4)
bot2=Button(text='Jugar',command=jugar)
caja_texto=Text(height=20,width=30)
bot.place(x=140,y=10,height=40,width=140)
entry.place(x=135,y=60,height=30,width=70)
bot2.place(x=215,y=60,height=30,width=70)
caja_texto.place(x=50,y=100,height=200,width=300)
ven.mainloop()
