#Manuel Ponce 3° 3° Grupo C

'''
Hacer una aplicación que permita emular el juego SIMON implementando componentes de la biblioteca Tkinter, utilizando botones, que irán modificando su color de fondo para ir mostrando la secuencia a reproducir por el usuario.

Los botones, para optimizar la implementación del manejo de eventos, deben estar en un vector.
Se debe importar la biblioteca time para poder utilizar la función sleep() para poder mostrar el color de la secuencia durante un tiempo.
Llevar un contador de secuencias como score.
Para poder implementar parámetros en el llamado a las acciones del botón, será necesario utilizar partial de la biblioteca functools.'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from functools import partial
import time
import random

def boton(ventana):
    botonizador=[]
    p=int(0)
    for c in range(4):
        p+=1
        if(p<=2):
            botonizador.append(Button(ventana,text='',activebackground=vecolor[c],command=partial(click,c)))
            botonizador[c].place(x=(c*100),y=50,height=100,width=100)
        else:
            botonizador.append(Button(ventana,text='',activebackground=vecolor[c],command=partial(click,c)))
            botonizador[c].place(x=((c-2)*100),y=150,height=100,width=100)
    return(botonizador)

def click(c):
    vecjugada.append(c)
    vecboton[c].configure(text=vecolor[c],background=vecolor[c])
    time.sleep(0.20)
    ventana.update()
    vecboton[c].configure(text='',background=vecolor[4])
    time.sleep(0.20)
    ventana.update()


def jugada():
    if(vecomp[0]==0):
        messagebox.showinfo(title='Error',message='Todavia no has dado a Comenzar')
    else:
        if(vecjugada==vecmaq):
            pop_jugada()
            jugada_maq(2)
            j[0]-=0.0075
        else:
            messagebox.showinfo(title='Que pena...',message='Has perdido')
            ventana.destroy()

def pop_jugada():
    for j in range(len(vecjugada)):
        vecjugada.pop()

def jugada_maq(x):
    if(vecomp[0]==0 or x==2):
        if(x==1):
            pop_jugada()
        vecomp[0]+=1
        vecmaq.append(random.randint(0,3))
        for i in vecmaq :
            vecboton[i].configure(text=vecolor[i],background=vecolor[i])
            time.sleep(j[0])
            ventana.update()
            vecboton[i].configure(text='',background=vecolor[4])
            time.sleep(j[0])
            ventana.update()
    else:
        messagebox.showinfo(title='Error',message='Ya has iniciado la partida')

j=[0.20]
vecomp=[0]
vecolor=[]
vecolor=['Red','Blue','Green','Yellow','Light Grey']
vecmaq=[]
vecjugada=[]
ventana = Tk()
ventana.geometry('200x300')
ventana.title('Simon de Ralph Baer y Howard J. Morrison')
vecboton=[]
vecboton=boton(ventana)

but2=Button(ventana,text='Comenzar',command=partial(jugada_maq,1))
but2.place(x=55,y=10,height=40,width=90)
but3=Button(ventana,text='Confirmar',command=(jugada))
but3.place(x=55,y=250,height=40,width=90)
