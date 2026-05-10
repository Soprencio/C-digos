#Manuel Ponce 3º 3º Grupo C

'''El juego se juega en un tablero de cuadrados , donde cada cuadrado es un piso o una pared. Algunos cuadrados del piso contienen cajas y algunos cuadrados del piso están
marcados como ubicaciones de almacenamiento. El jugador está confinado al tablero y puede moverse horizontal o verticalmente sobre casillas vacías (nunca a través de
paredes o cajas). El jugador puede mover una caja caminando hacia ella y empujándola hacia la casilla más allá. Las cajas no se pueden tirar y no se pueden empujar a
cuadrados con paredes u otras cajas. El número de cajas es igual al número de ubicaciones de almacenamiento. El rompecabezas se resuelve cuando todas las cajas se colocan
en lugares de almacenamiento. Desarrollar una aplicación Python que permita jugar este juego. Debiendo implementar el escenario a partir de los datos almacenados en una
matriz, donde el 0 (cero) representa los lugares por donde desplazarse, el 1 (uno) las paredes, 2 (dos) las cajas fijas, 3 (tres) las cajas a acomodar o movibles.
Tener en cuenta que las imágenes deben tener todas el mismo tamaño.'''

import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from functools import partial

def cargar():
    m=[None]*veclv[0]
    for i in range(veclv[0]):
        m[i]=[None]*veclv[1]
    return(m)

def imagenes(lv):
    for j in range(veclv[0]):
        label=[]
        for i in range(veclv[1]):
            label.append(Label(image=imagenzoom[mat[j][i]]))
        matimg[j]=label
    for c in range(veclv[0]):
        for f in range(veclv[1]):
            if(lv!=4 and lv!=5):
                matimg[c][f].place(x=((c*80)+160),y=((f*80)+100),height=80,width=80)
            else:
                matimg[c][f].place(x=((c*64)+60),y=((f*64)+100),height=64,width=64)



def boton():
    botonizador=[]
    botonizador.append(Button(image=imagenzoom[5],command=partial(reinicio)))
    botones[0]=botonizador[0]
    botones[0].place(x=(440),y=(0),height=120,width=120)

def reinicio():
    for i in range(veclv[0]):
        for j in range(veclv[1]):
            mat[i][j]=mat_or[i][j]
            matimg[i][j].configure(image=imagenzoom[mat_or[i][j]])
    aux2[0]=0
    ventana.update()

def click(event):
    if(0==0):
        aux[2]=0
        for c in range(veclv[0]):
            for f in range(veclv[1]):
                if(mat[c][f]==6):
                    aux[0]=c
                    aux[1]=f
        if(event.keysym=='Left'):
            if(mat[aux[0]-1][aux[1]]==0 or mat[aux[0]-1][aux[1]]==4):
                j=mat[aux[0]-1][aux[1]]
                matimg[aux[0]][aux[1]].configure(image=imagenzoom[aux2[0]])
                mat[aux[0]][aux[1]]=aux2[0]
                matimg[aux[0]-1][aux[1]].configure(image=imagenzoom[6])
                mat[aux[0]-1][aux[1]]=6
                aux2[0]=j
                ventana.update()
            elif(mat[aux[0]-1][aux[1]]==2 or mat[aux[0]-1][aux[1]]==3):
                if(mat[aux[0]-2][aux[1]]==0 or mat[aux[0]-2][aux[1]]==4):
                    k=mat[aux[0]-2][aux[1]]
                    matimg[aux[0]][aux[1]].configure(image=imagenzoom[aux2[0]])
                    mat[aux[0]][aux[1]]=aux2[0]
                    if(mat[aux[0]-1][aux[1]]==2):
                        matimg[aux[0]-1][aux[1]].configure(image=imagenzoom[6])
                        mat[aux[0]-1][aux[1]]=6
                        aux2[0]=0
                        if(mat[aux[0]-2][aux[1]]==4):
                            matimg[aux[0]-2][aux[1]].configure(image=imagenzoom[3])
                            mat[aux[0]-2][aux[1]]=3
                        elif(mat[aux[0]-2][aux[1]]==0):
                            matimg[aux[0]-2][aux[1]].configure(image=imagenzoom[2])
                            mat[aux[0]-2][aux[1]]=2
                    elif(mat[aux[0]-1][aux[1]]==3):
                        matimg[aux[0]-1][aux[1]].configure(image=imagenzoom[6])
                        mat[aux[0]-1][aux[1]]=6
                        aux2[0]=4
                        if(mat[aux[0]-2][aux[1]]==4):
                            matimg[aux[0]-2][aux[1]].configure(image=imagenzoom[3])
                            mat[aux[0]-2][aux[1]]=3
                        elif(mat[aux[0]-2][aux[1]]==0):
                            matimg[aux[0]-2][aux[1]].configure(image=imagenzoom[2])
                            mat[aux[0]-2][aux[1]]=2
            ventana.update()
                    
        if(event.keysym=='Right'):
            if(mat[aux[0]+1][aux[1]]==0 or mat[aux[0]+1][aux[1]]==4):
                j=mat[aux[0]+1][aux[1]]
                matimg[aux[0]][aux[1]].configure(image=imagenzoom[aux2[0]])
                mat[aux[0]][aux[1]]=aux2[0]
                matimg[aux[0]+1][aux[1]].configure(image=imagenzoom[6])
                mat[aux[0]+1][aux[1]]=6
                aux2[0]=j
                ventana.update()
            elif(mat[aux[0]+1][aux[1]]==2 or mat[aux[0]+1][aux[1]]==3):
                if(mat[aux[0]+2][aux[1]]==0 or mat[aux[0]+2][aux[1]]==4):
                    k=mat[aux[0]+2][aux[1]]
                    matimg[aux[0]][aux[1]].configure(image=imagenzoom[aux2[0]])
                    mat[aux[0]][aux[1]]=aux2[0]
                    if(mat[aux[0]+1][aux[1]]==2):
                        matimg[aux[0]+1][aux[1]].configure(image=imagenzoom[6])
                        mat[aux[0]+1][aux[1]]=6
                        aux2[0]=0
                        if(mat[aux[0]+2][aux[1]]==4):
                            matimg[aux[0]+2][aux[1]].configure(image=imagenzoom[3])
                            mat[aux[0]+2][aux[1]]=3
                        elif(mat[aux[0]+2][aux[1]]==0):
                            matimg[aux[0]+2][aux[1]].configure(image=imagenzoom[2])
                            mat[aux[0]+2][aux[1]]=2
                    elif(mat[aux[0]+1][aux[1]]==3):
                        matimg[aux[0]+1][aux[1]].configure(image=imagenzoom[6])
                        mat[aux[0]+1][aux[1]]=6
                        aux2[0]=4
                        if(mat[aux[0]+2][aux[1]]==4):
                            matimg[aux[0]+2][aux[1]].configure(image=imagenzoom[3])
                            mat[aux[0]+2][aux[1]]=3
                        elif(mat[aux[0]+2][aux[1]]==0):
                            matimg[aux[0]+2][aux[1]].configure(image=imagenzoom[2])
                            mat[aux[0]+2][aux[1]]=2
            ventana.update()
                
        if(event.keysym=='Up'):
            if(mat[aux[0]][aux[1]-1]==0 or mat[aux[0]][aux[1]-1]==4):
                j=mat[aux[0]][aux[1]-1]
                matimg[aux[0]][aux[1]].configure(image=imagenzoom[aux2[0]])
                mat[aux[0]][aux[1]]=aux2[0]
                matimg[aux[0]][aux[1]-1].configure(image=imagenzoom[6])
                mat[aux[0]][aux[1]-1]=6
                aux2[0]=j
                ventana.update()
            elif(mat[aux[0]][aux[1]-1]==2 or mat[aux[0]][aux[1]-1]==3):
                if(mat[aux[0]][aux[1]-2]==0 or mat[aux[0]][aux[1]-2]==4):
                    k=mat[aux[0]][aux[1]-2]
                    matimg[aux[0]][aux[1]].configure(image=imagenzoom[aux2[0]])
                    mat[aux[0]][aux[1]]=aux2[0]
                    if(mat[aux[0]][aux[1]-1]==2):
                        matimg[aux[0]][aux[1]-1].configure(image=imagenzoom[6])
                        mat[aux[0]][aux[1]-1]=6
                        aux2[0]=0
                        if(mat[aux[0]][aux[1]-2]==4):
                            matimg[aux[0]][aux[1]-2].configure(image=imagenzoom[3])
                            mat[aux[0]][aux[1]-2]=3
                        elif(mat[aux[0]][aux[1]-2]==0):
                            matimg[aux[0]][aux[1]-2].configure(image=imagenzoom[2])
                            mat[aux[0]][aux[1]-2]=2
                    elif(mat[aux[0]][aux[1]-1]==3):
                        matimg[aux[0]][aux[1]-1].configure(image=imagenzoom[6])
                        mat[aux[0]][aux[1]-1]=6
                        aux2[0]=4
                        if(mat[aux[0]][aux[1]-2]==4):
                            matimg[aux[0]][aux[1]-2].configure(image=imagenzoom[3])
                            mat[aux[0]][aux[1]-2]=3
                        elif(mat[aux[0]][aux[1]-2]==0):
                            matimg[aux[0]][aux[1]-2].configure(image=imagenzoom[2])
                            mat[aux[0]][aux[1]-2]=2
            ventana.update()
                
        if(event.keysym=='Down'):
            if(mat[aux[0]][aux[1]+1]==0 or mat[aux[0]][aux[1]+1]==4):
                j=mat[aux[0]][aux[1]+1]
                matimg[aux[0]][aux[1]].configure(image=imagenzoom[aux2[0]])
                mat[aux[0]][aux[1]]=aux2[0]
                matimg[aux[0]][aux[1]+1].configure(image=imagenzoom[6])
                mat[aux[0]][aux[1]+1]=6
                aux2[0]=j
                ventana.update()
            elif(mat[aux[0]][aux[1]+1]==2 or mat[aux[0]][aux[1]+1]==3):
                if(mat[aux[0]][aux[1]+2]==0 or mat[aux[0]][aux[1]+2]==4):
                    k=mat[aux[0]][aux[1]+2]
                    matimg[aux[0]][aux[1]].configure(image=imagenzoom[aux2[0]])
                    mat[aux[0]][aux[1]]=aux2[0]
                    if(mat[aux[0]][aux[1]+1]==2):
                        matimg[aux[0]][aux[1]+1].configure(image=imagenzoom[6])
                        mat[aux[0]][aux[1]+1]=6
                        aux2[0]=0
                        if(mat[aux[0]][aux[1]+2]==4):
                            matimg[aux[0]][aux[1]+2].configure(image=imagenzoom[3])
                            mat[aux[0]][aux[1]+2]=3
                        elif(mat[aux[0]][aux[1]+2]==0):
                            matimg[aux[0]][aux[1]+2].configure(image=imagenzoom[2])
                            mat[aux[0]][aux[1]+2]=2
                    elif(mat[aux[0]][aux[1]+1]==3):
                        matimg[aux[0]][aux[1]+1].configure(image=imagenzoom[6])
                        mat[aux[0]][aux[1]+1]=6
                        aux2[0]=4
                        if(mat[aux[0]][aux[1]+2]==4):
                            matimg[aux[0]][aux[1]+2].configure(image=imagenzoom[3])
                            mat[aux[0]][aux[1]+2]=3
                        elif(mat[aux[0]][aux[1]+2]==0):
                            matimg[aux[0]][aux[1]+2].configure(image=imagenzoom[2])
                            mat[aux[0]][aux[1]+2]=2
            ventana.update()
        for c in range(veclv[0]):
            for f in range(veclv[1]):
                if(mat[c][f]==3):
                    aux[2]+=1
        if(aux[2]==veclv[2]):
            messagebox.showinfo(title='Felicidades',message='Has colocado todas las cajas en las baldosas de almacenamiento')
                    
def crear_img(lv):
    if(lv!=4 and lv!=5):
        for c in range(9):
                imagen[c]=PhotoImage(file='sokoban/'+imagen[c]+'.png')
                imagenzoom.append(imagen[c].zoom(5))
    else:
        for c in range(9):
                imagen[c]=PhotoImage(file='sokoban/'+imagen[c]+'.png')
                imagenzoom.append(imagen[c].zoom(4))

def lista_lv(lv):
    if(lv==1):
        matr=[[1,1,1,1,1,1,1,1,1],[1,1,4,7,4,0,2,0,1],[1,1,0,7,7,7,0,0,1],[1,6,0,0,7,0,3,0,1],[1,0,2,2,2,4,2,4,1],[1,0,0,4,0,0,2,0,1],[1,1,1,1,1,1,4,0,1],[1,1,1,1,1,1,1,1,1]]
        veclv[0]=8
        veclv[1]=9
        veclv[2]=7
        return(matr)
    elif(lv==2):
        matf=[[1,1,1,1,1,1,1,1],[1,1,1,1,1,0,0,1],[1,1,1,1,1,2,4,1],[1,0,0,0,7,0,0,1],[1,0,2,0,0,4,0,1],[1,1,1,0,7,0,4,1],[1,1,1,0,0,0,0,1],[1,1,1,2,2,4,0,1],[1,1,0,6,0,0,0,1],[1,1,1,1,1,1,1,1]]
        veclv[0]=10
        veclv[1]=8
        veclv[2]=4
        return(matf)
    elif(lv==3):
        matd=[[1,1,1,1,1,1,1,1,1],[1,1,0,0,0,0,0,0,1],[1,0,0,2,4,4,4,0,1],[1,0,0,7,1,1,7,2,1],[1,0,2,0,1,1,0,4,1],[1,0,2,0,1,1,7,0,1],[1,0,0,4,1,1,0,0,1],[1,0,2,1,1,1,1,0,1],[1,1,6,1,1,1,1,0,1],[1,1,1,1,1,1,1,1,1]]
        veclv[0]=10
        veclv[1]=9
        veclv[2]=5
        return(matd)
    elif(lv==4):
        matg=[[1,1,1,1,1,1,1,1,1,1,1,1,1],[1,0,0,0,0,1,4,4,4,4,4,1,1],[1,0,2,2,0,1,4,4,4,4,4,1,1],[1,0,0,0,1,1,0,0,0,0,0,0,1],[1,0,0,0,1,1,0,0,0,0,0,0,1],[1,1,1,0,1,1,0,0,0,0,0,1,1],[1,1,1,0,6,1,1,1,7,7,0,1,1],[1,1,1,0,1,1,1,1,7,7,0,1,1],[1,1,1,0,1,1,0,2,0,0,2,1,1],[1,0,0,2,1,1,0,0,2,2,0,1,1],[1,0,2,0,2,0,0,0,0,0,2,1,1],[1,0,0,0,0,7,0,0,0,0,0,1,1],[1,1,1,1,1,1,0,0,0,0,0,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1]]
        veclv[0]=14
        veclv[1]=13
        veclv[2]=10
        return(matg)
    elif(lv==5):
        matk=[[1,1,1,1,1,1,1,1,1,1],[1,4,4,4,4,4,1,1,1,1],[1,4,4,4,4,4,1,1,1,1],[1,0,0,0,0,0,1,0,0,1],[1,0,0,0,0,0,1,2,0,1],[1,1,1,1,0,1,1,0,0,1],[1,0,0,2,0,0,0,0,0,1],[1,0,2,1,6,7,7,2,1,1],[1,0,0,1,0,0,7,0,0,1],[1,0,0,1,1,0,2,2,0,1],[1,0,2,1,1,2,0,0,0,1],[1,1,0,0,0,0,2,2,0,1],[1,1,0,0,0,1,0,0,0,1],[1,1,1,1,1,1,1,1,1,1]]
        veclv[0]=14
        veclv[1]=10
        veclv[2]=10
        return(matk)

ventana= Tk()
ventana.geometry('1000x1000')
ventana.title('sokoban')
imagenzoom=[]
flechazoom=[]
imagen=['Suelo_0','Pared_1','Caja_2','Caja_inmo_3','Almacenamiento_4','Reinicio','Persona','Caja_cor_7','vacio']
aux2=[0,0,0]
aux=[0,0,0]
veclv=[0,0,0]
a=[1]
lv=int(input('Ingrese nivel a jugar (1-5): '))
while(lv>5 or lv<1):
    lv=int(input('Ese nivel no existe, ingrese otro(1-5): '))
mat=lista_lv(lv)
mat_or=cargar()
for c in range(veclv[0]):
    for f in range(veclv[1]):
        mat_or[c][f]=mat[c][f]
crear_img(lv)
matimg=cargar()
imagenes(lv)
botones=[None]
boton()
ventana.bind('<Key>', click)

ventana.mainloop()
