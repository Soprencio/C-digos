#Manuel Ponce 3º 3º Grupo C

'''El juego de la memoria consiste en un grupo de pares imágenes que deben ser descubiertas de forma consecutiva hasta descubrir todas las imágenes.
El jugador obtiene como puntuación la cantidad de clicks realizados para descubrir las imágenes, siendo el que haya utilizado menos clicks el que más puntos obtenga.
Para la resolución del ejercicio, se deberá tener en cuenta que hay que generar una matriz de 4 filas x 8 columnas numérica, donde se almacenarán los pares de valores entre
0 y 15, que representan a los valores de las imágenes en una segunda matriz de 4 x 8 donde se almacenarán botones con las imágenes almacenadas en un vector de 16 imágenes.'''

# Para el código se utilizó la función subsample, no explicada en clase, para poder ajustar el tamaño de las imagenes. El Memotest se hizo en base a Pokémon

import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from functools import partial
import time

def cargar():
    m=[None]*8
    for i in range(8):
        m[i]=[None]*4
    return(m)

def cargar2():
    m=[None]*4
    for i in range(4):
        m[i]=[None]*8
    return(m)

def crear_mat():
    for j in range(8):
        botonizador=[]
        for i in range(4):
            botonizador.append(Button(image=imagen2zoom,command=partial(click,i,j)))
        matimg[j]=botonizador
    for c in range(8):
        for f in range(4):
            matimg[c][f].place(x=((c*120)+120),y=((f*120)+120),height=120,width=120)
        
def cargar_mat():
    for i in range(4):
        for j in range(8):
            k=random.randint(0,15)
            while(veclista[k]>=2):
                k=random.randint(0,15)
            matnum[i][j]=k
            veclista[k]+=1

def cargalista():
    for i in range(16):
        veclista.append(0)

def click(i,j):
    if(vecant[0]==1):
        vecant[5]+=1
        lbl.configure(text=vecant[5])
        vecant[0]=2
        vecant[1]=i
        vecant[2]=j
        matimg[vecant[2]][vecant[1]].configure(command='None',image=imagenzoom[matnum[i][j]])
        ventana.update()
        if(matnum[vecant[1]][vecant[2]]==matnum[vecant[3]][vecant[4]]):
            matimg[vecant[2]][vecant[1]].configure(command='None')
            ventana.update()
            vecant[6]+=1
            if(vecant[6]==16):
                messagebox.showinfo(title='Felicidades',message='Has ganado en '+str(vecant[5])+' clicks, intenta ganar con menos clicks')
            for g in range(5):
               vecant[g]=0
        else:
            time.sleep(0.5)
            matimg[vecant[2]][vecant[1]].configure(image=imagen2zoom)
            matimg[vecant[4]][vecant[3]].configure(image=imagen2zoom)
            matimg[vecant[4]][vecant[3]].configure(command=partial(click,vecauxil[0],vecauxil[1]))
            matimg[vecant[2]][vecant[1]].configure(command=partial(click,i,j))
            ventana.update()
            for g in range(5):
                vecant[g]=0

    elif(vecant[0]==0):
        vecant[5]+=1
        lbl.configure(text=vecant[5])
        vecant[0]=2
        vecant[3]=i
        vecant[4]=j
        ventana.update()
        matimg[vecant[4]][vecant[3]].configure(command='None',image=imagenzoom[matnum[i][j]])
        vecauxil[0]=i
        vecauxil[1]=j
        vecant[0]=1



ventana = Tk()
ventana.geometry('1200x800')
ventana.title('memotest')
imagenzoom=[]
imagen2zoom=[]
imagen=['pikachu','eevee','charmander','squirtle','bulbasaur','charizard','blastoise','venusaur','snorlax','mewtwo','mew','dragonite','pidgey','caterpie','rattata','aerodactyl']
for c in range(16):
    imagen[c]=PhotoImage(file='img/'+imagen[c]+'.png')
    imagenzoom.append(imagen[c].subsample(6))
imagen2=PhotoImage(file='img/pokemon.png')
imagen2zoom.append(imagen2.subsample(11))
vecauxil=[0,0]
vecant=[0,0,0,0,0,0,0]
veclista=[]
cargalista()
matnum=[]
lbl=Label(text=vecant[5])
lbl.place(x=570,y=600,height=120,width=60)
matnum=cargar2()
cargar_mat()
matimg=cargar()
crear_mat()
ventana.mainloop()
