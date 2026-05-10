#Manuel Ponce 3° 3° Grupo C
'''Hacer una aplicación con Tkinter, que permita seleccionar el films y muestre a los personajes que aparecen en el mismo.
Tambien que permita seleccionar el homeworld y muestre todos los personajes que nacieron en ese sitio.

Tener en cuenta que un personaje puede aparecer en varios films y figuran entre comillas dobles ("...")

- La selección de los elementos deben realizarse con Combobox.
- La información de los Combobox se deben tomar del archivo.
- Las listas de resultados deben realizarse en Treeview y se muestran todos los datos (15 columnas).
- Los listados deben aparecer ordenados por el nombre de menor a mayor.'''

from tkinter import *
from tkinter import ttk
from functools import partial

def films(ventana):
    auxiliar=open('auxiliar.txt','w',encoding='utf-8')
    star=open('star_wars_character_dataset.csv','r',encoding='utf-8')
    aux3=int(0)
    aux4=''
    booliano=int(0)
    for c in star :
        aux=c
        for i in aux :
            if(i==',' and booliano==0):
                aux4+=str(i)
            elif(i=='"' and booliano==1):
                booliano=0
                aux4+=str(i)
            elif(i=='"' and booliano==0):
                booliano=1
                aux4+=str(i)
            elif(i==',' and booliano==1):
                aux4+=('.')
            elif(i!=','):
                aux4+=str(i)
    auxiliar.write(aux4)
    star.close()
    auxiliar.close()
    auxiliar=open('auxiliar.txt','r',encoding='utf-8')
    for i in auxiliar :
        aux=i[:-1]
        fila=aux.split(',')
        e=int(0)
        for c in fila :
            if(c=='films'):
                aux2[0]=e
            e+=1
    auxiliar.close()
    auxiliar=open('auxiliar.txt','r',encoding='utf-8')
    aux5=int(0)
    for i in auxiliar :
        aux4=''
        aux=i[:-1]
        fila=aux.split(',')
        for c in fila[11] :
            if(c!='.'):
                if(c!='"'):
                    if(c==' ' and aux5==0):
                        aux4+='_'
                    elif(c!=' '):
                        aux4+=str(c)
                        aux5=0
            else:
                aux4+=','
                aux5=1
        fila=aux4.split(',')
        for c in range(len(fila)):
            if(c==0 and aux3==0):
                if(fila[c]!='films'):
                    filmes.append(fila[c])
            else:
                aux4=int(0)
                for j in range(len(filmes)):
                    if(fila[c]==filmes[j]):
                        aux4+=1
                if(aux4==0):
                    if(fila[c]!='films'):
                        filmes.append(fila[c])
            
        aux3+=1
    auxiliar.close()
    auxiliar=open('auxiliar.txt','r',encoding='utf-8')
    aux3=int(0)
    for i in auxiliar :
        aux4=''
        aux=i[:-1]
        fila=aux.split(',')
        if(aux3==0):
            if(fila[9]!='homeworld'):
                homes.append(fila[9])
        else:
            aux4=int(0)
            for j in range(len(homes)):
                if(fila[9]==homes[j]):
                    aux4+=1
            if(aux4==0):
                if(fila[9]!='homeworld'):
                    homes.append(fila[9])
        aux3+=1

def click(x,buton,event):
    buton[x].configure(state='normal')

def combobox(ventana):
    combo.append(ttk.Combobox(ventana,state='readonly',values=filmes))
    combo.append(ttk.Combobox(ventana,state='readonly',values=homes))
    buton.append(Button(ventana,text='Treeview Films',state='disable',command=partial(tree,ventana)))
    buton.append(Button(ventana,text='Treeview Homeworld',state='disable',command=partial(tree2,ventana)))
    combo[0].bind('<<ComboboxSelected>>',partial(click,0,buton))
    combo[1].bind('<<ComboboxSelected>>',partial(click,1,buton))
    for c in range(2):
        combo[c].place(x=(350*c)+25,y=100,height=30,width=250)
        buton[c].place(x=(350*c)+25,y=160,height=30,width=250)

def tree2(ventana):
    auxiliar=open('auxiliar.txt','r',encoding='utf-8')
    auxiliar2=open('auxiliar2.txt','w',encoding='utf-8')
    for i in auxiliar :
        aux=i[:-1]
        fila=aux.split(',')
        if(fila[9]==str(combo[1].get())):
            for k in range(len(fila)):
                if(k+1<len(fila)):
                    auxiliar2.write(str(fila[k])+',')
                else:
                    auxiliar2.write(str(fila[k]))
            auxiliar2.write('\n')
    auxiliar.close()
    auxiliar2.close()

    menor()
    
    auxiliar=open('auxiliar.txt','r',encoding='utf-8')
    auxiliar2=open('auxiliar2.txt','r',encoding='utf-8')
    aux=auxiliar.readline()
    fila=aux.split(',')
    tl=Toplevel()
    tl.geometry('1400x500+500+10')
    tl.title('Treeview Films')
    Star_frame=Frame(tl)
    Star_frame.pack(pady=10)
    Tree=ttk.Treeview(Star_frame,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14),show='headings',selectmode='extended')
    for c in range(13):
        Tree.heading(c+1,text=fila[c])
        if(c<11):
            Tree.column(c+1,width=150)
        elif(c==11):
            Tree.column(c+1,width=1000)
        else:
            Tree.column(c+1,width=250)
        
    for c in auxiliar2 :
        Tree.insert('','end',values=c[:-1].split(',',14))
    Tree.pack()
    auxiliar.close()
    auxiliar2.close()

def tree(ventana):
    auxiliar=open('auxiliar.txt','r',encoding='utf-8')
    auxiliar2=open('auxiliar2.txt','w',encoding='utf-8')
    aux3=int(0)
    for i in auxiliar :
        aux4=''
        aux=i[:-1]
        fila=aux.split(',')
        for c in fila[11] :
            if(c!='.'):
                if(c!='"'):
                    if(c==' ' and aux5==0):
                        aux4+='_'
                    elif(c!=' '):
                        aux4+=str(c)
                        aux5=0
            else:
                aux4+=','
                aux5=1
        fila=aux4.split(',')
        aux4=int(0)
        for c in fila :
            if(c==combo[0].get()):
                aux4+=1
        if(aux4>0):
            fila=aux.split(',')
            for k in range(len(fila)):
                if(k+1<len(fila)):
                    auxiliar2.write(str(fila[k])+',')
                else:
                    auxiliar2.write(str(fila[k]))
            auxiliar2.write('\n')
    auxiliar.close()
    auxiliar2.close()

    menor()

    auxiliar=open('auxiliar.txt','r',encoding='utf-8')
    auxiliar2=open('auxiliar2.txt','r',encoding='utf-8')
    aux=auxiliar.readline()
    fila=aux.split(',')
    tl=Toplevel()
    tl.geometry('1400x500+500+10')
    tl.title('Treeview Films')
    Star_frame=Frame(tl)
    Star_frame.pack(pady=10)
    Tree=ttk.Treeview(Star_frame,columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14),show='headings',selectmode='extended')
    for c in range(13):
        Tree.heading(c+1,text=fila[c])
        if(c<11):
            Tree.column(c+1,width=150)
        elif(c==11):
            Tree.column(c+1,width=800)
        else:
            Tree.column(c+1,width=250)
        
    for c in auxiliar2 :
        Tree.insert('','end',values=c[:-1].split(',',14))
    Tree.pack()
    auxiliar.close()
    auxiliar2.close()

def menor():
    auxiliar2=open('auxiliar2.txt','r',encoding='utf-8')
    cont=int(0)
    for c in auxiliar2:
        cont+=1
    auxiliar2.close()
    for c in range(cont):
        auxiliar2=open('auxiliar2.txt','r',encoding='utf-8')
        temporal=open('temporal.txt','w',encoding='utf-8')
        ordenado=open('ordenado.txt','a',encoding='utf-8')
        e=int(0)
        aux=int(0)
        for c in auxiliar2 :
            fila=c.split(',')
            if(e==0):
                p=fila
                aux=e
            else:
                if(fila<p):
                    p=fila
                    aux=e
            e+=1
        for c in range(len(p)):
            if(c+1<len(p)):
                ordenado.write(p[c]+',')
            else:
                ordenado.write(p[c])
        e=int(0)
        auxiliar2.close()
        auxiliar2=open('auxiliar2.txt','r',encoding='utf-8')
        for c in auxiliar2 :
            aux3=c[:-1]
            fila=aux3.split(',')
            if(aux!=e):
                for i in range(len(fila)):
                    if(i+1<len(fila)):
                        temporal.write(fila[i]+',')
                    else:
                        temporal.write(fila[i])
                temporal.write('\n')
            e+=1
        temporal.close()
        auxiliar2.close()
        auxiliar2=open('auxiliar2.txt','w',encoding='utf-8')
        temporal=open('temporal.txt','r',encoding='utf-8')
        e=int(0)
        for i in temporal:
            aux=i[:-1]
            fila=aux.split(',')
            for c in range(len(fila)):
                if(c+1<len(fila)):
                    auxiliar2.write(fila[c]+',')
                else:
                    auxiliar2.write(fila[c])
            auxiliar2.write('\n')
            e+=1
        temporal.close()
        auxiliar2.close()
    ordenado.close()
    auxiliar2=open('auxiliar2.txt','w',encoding='utf-8')
    ordenado=open('ordenado.txt','r',encoding='utf-8')
    e=int(0)
    for i in ordenado:
        aux=i[:-1]
        fila=aux.split(',')
        for c in range(len(fila)):
            if(c+1<len(fila)):
                auxiliar2.write(fila[c]+',')
            else:
                auxiliar2.write(fila[c])
        auxiliar2.write('\n')
        e+=1   
    auxiliar2.close()
    ordenado.close()
    ordenado=open('ordenado.txt','w',encoding='utf-8')
    ordenado.close()

auxiliar=open('auxiliar.txt','w',encoding='utf-8')
auxiliar2=open('auxiliar2.txt','w',encoding='utf-8')
auxiliar.close()
auxiliar2.close()
ventana=Tk()
ventana.geometry('700x300')
ventana.title('Star Wars')
aux2=[0]
filmes=[]
combo=[]
buton=[]
homes=[]

films(ventana)
combobox(ventana)

ventana.mainloop()
