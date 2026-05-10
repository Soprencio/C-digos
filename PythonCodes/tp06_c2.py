#Manuel Ponce 3° 3° Grupo C
'''Se necesita hacer una aplicación en Python para gestionar las notas de los alumnos de la escuela.
Para ello se dispone almacenar la información de los alumnos, de las materias y las notas obtenidas en cada materia por cada alumno.
Esta información será almacenada en archivos.

alumnos.dat
id_alu
dni
apellido
nombre
email
curso
división

notas.dat
id_nota
id_alu
id_mat
nota_1
nota_2
nota_3
nota_4

materias.dat
id_mat
nombre
curso

id_alu - id_nota - id_mat: Son valores numéricos únicos, que identifican a cada alumno, cada nota y cada materia y deben incrementarse automáticamente al agregar un
nuevo registro en cada uno de los archivos.
Notas:
El programa debe permitir agregar un dato nuevo de cada uno de los archivos, llamando a dicho proceso ALTA de datos. 
Se podrá eliminar un registro de datos de cada uno de los archivos si fuera necesario, proceso que se denomina BAJA. 
También se deberá poder modificar un dato ya existente en cualquiera de los archivos, proceso que se denomina MODIFICACIÓN de datos.
Los datos de los archivos deben poder ser visualizados, proceso que se llama LISTADOS.
El Email de los alumnos debe estar validado de forma tal que debe existir un @ y un punto no adyacente luego del arroba y tampoco al final del email.
Será necesario tener en cuenta la implementación de uno o varios archivos que almacene el último id_xxx de cada archivo, donde solo se almacenará un dato y éste será
reemplazado cada vez que se genere un nuevo registro en cada uno de los archivos. Se deben implementar los componentes Combobox() para la selección de Curso y
División en el alta de alumnos, y también para la selección de Alumnos y Materias en el alta de notas.
Los listados deben implementar el componente TreeView() que figura en el blog.
Se deben entregar el archivo del código y los archivos con los datos.'''

import random
import time
from tkinter import *
from tkinter import messagebox
from functools import partial
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Toplevel


def cargar():
  m=[None]*4
  for i in range(4):
      m[i]=[None]*4
  return(m)




def labeles():
  for i in range(4):
      labels.append(Label(text=nom_l[i]))
  for c in range(4):
      labels[c].place(x=(c*150)+35,y=20,height=30,width=60)




def botones():
  for i in range(4):
      boton=[]
      for j in range(4):
          if(i==0 and j==3):
              boton.append(Button(text=nom_b[3],command=partial(click,i,j,ventana)))
          else:
              boton.append(Button(text=nom_b[i],command=partial(click,i,j,ventana)))              
      botons[i]=boton
  for c in range(4):
      for f in range(4):
          if(f!=3 or c==0):
              botons[c][f].place(x=(f*150)+10,y=(c*30)+60,height=30,width=110)




def click(i,j,ventana):
  for c in range(4):
      for f in range(4):
          if(f!=3 or c==0):
              botons[c][f].configure(state='disable')
  alta_a= Toplevel()
  alta_a.geometry('400x300')
  alta_a.protocol('WM_DELETE_WINDOW',partial(cerrar,alta_a,1))


  if(i==0):
      if(j==0):
          alta_a.title('Alta de Alumno')
          id_a=open('id_a.dat.txt','w',encoding='utf-8')
          id_a.write(str(vec_id[0]))
          id_a.close()
          alta_alum(alta_a)
          agre_a=Button(alta_a,text='Agregar',command=partial(agregar,alta_a))
          agre_a.place(x=330,y=260,height=30,width=60)
      elif(j==1):
          alta_a.title('Alta de Nota')
          id_n=open('id_n.dat.txt','w',encoding='utf-8')
          id_n.write(str(vec_id[1]))
          id_n.close()
          alta_nota(alta_a)
          agre_n=Button(alta_a,text='Agregar',command=partial(agregar3,alta_a))
          agre_n.place(x=330,y=260,height=30,width=60)
      elif(j==2):
          alta_a.title('Alta de Materia')
          id_m=open('id_m.dat.txt','w',encoding='utf-8')
          id_m.write(str(vec_id[2]))
          id_m.close()
          alta_mat(alta_a)
          agre_m=Button(alta_a,text='Agregar',command=partial(agregar2,alta_a))
          agre_m.place(x=330,y=260,height=30,width=60)
      elif(j==3):
          alta_a.title('Selección de Boletin') 
          boleta(alta_a)
  elif(i==1):
      if(j==0):
          alta_a.title('Baja de Alumno')
          baja_alum(alta_a)
          borra_a=Button(alta_a,text='Borrar',command=partial(borrar,alta_a))
          borra_a.place(x=330,y=260,height=30,width=60)
      elif(j==1):
          alta_a.title('Baja de Nota')
          baja_nota(alta_a)
          borra_n=Button(alta_a,text='Borrar',command=partial(borrar3,alta_a))
          borra_n.place(x=330,y=260,height=30,width=60)
      elif(j==2):
          alta_a.title('Baja de Materia')
          baja_mat(alta_a)
          borra_m=Button(alta_a,text='Borrar',command=partial(borrar2,alta_a))
          borra_m.place(x=330,y=260,height=30,width=60)
  elif(i==2):
      if(j==0):
          alta_a.title('Modificar Alumno')
          modificar_alu(alta_a)
          camb_a=Button(alta_a,text='Cambiar',command=partial(modificar,alta_a))
          camb_a.place(x=330,y=260,height=30,width=60)
      elif(j==1):
          alta_a.title('Modificar Nota')
          modificar_not(alta_a)
          camb_n=Button(alta_a,text='Cambiar',command=partial(modificar3,alta_a))
          camb_n.place(x=330,y=260,height=30,width=60)
      elif(j==2):
          alta_a.title('Modificar Materia')
          modificar_mat(alta_a)
          camb_m=Button(alta_a,text='Cambiar',command=partial(modificar2,alta_a))
          camb_m.place(x=330,y=260,height=30,width=60)
  elif(i==3):
      if(j==0):
          alta_a.geometry('1600x400')
          alta_a.title('Listado de Alumno')
          listado_a(alta_a,0)
      elif(j==1):
          alta_a.geometry('1600x400')
          alta_a.title('Listado de Notas')
          listado_n(alta_a,1)
      elif(j==2):
          alta_a.geometry('650x400')
          alta_a.title('Listado de Materias')
          listado_m(alta_a,2)



def boleta(alta_a):
    for i in range(len(texte)):
        texte.pop()
    for i in range(len(ent)):
        ent.pop()
    texte.append(Label(alta_a,text='Id Alu a Hacer Boletín'))
    nums=idedes3(0)
    ent.append(ttk.Combobox(alta_a,state='readonly',values=nums))
    texte[0].place(x=20,y=20,height=25,width=150)
    ent[0].place(x=180,y=20,height=25,width=200)
    confir=Button(alta_a,text='Confirmar',command=partial(boletin,alta_a))
    confir.place(x=330,y=260,height=30,width=70)

def boletin(alta_a):
    if(ent[0].get()!=''):
        alta_b=Toplevel()
        alta_b.geometry('1600x600')
        alta_b.title('Boletín')
        alta_b.protocol('WM_DELETE_WINDOW',partial(cerrar,alta_b,1))
        cb=ent[0].get()
        alta_a.destroy()
        listado_boletines(alta_b,cb)
    else:
        messagebox.showinfo(title='Error',message='Ingrese algún dato')
         
def modificar3(alta_a):
   auxi=int(0)
   for i in range(3,7):
      aux=ent[i].get()
      if(len(aux)<1 and auxi==0):
          auxi=1
          messagebox.showinfo(title='Error',message='Por lo menos coloca 2 caracteres')
   aux=int(0)
   if(auxi==0):
       notas=open('notas.dat.txt','r',encoding='utf-8')
       auxiliar=open('auxiliar.txt','w',encoding='utf-8')
       for i in notas :
           if(i==ent[0].get()+'°'+'\n' or aux>0):
               if(aux==0):
                   print('thepep')
                   auxiliar.write(i)
                   aux=1
               else:
                   if(aux==1 or aux==2):
                       auxiliar.write(vec_aux2[aux-1])
                       print(str(vec_aux2[0]),str(vec_aux2[1]))
                       aux+=1
                   else:
                       print(ent[aux].get())
                       auxiliar.write(ent[aux].get()+'\n')
                       aux+=1
                       if(aux==7):
                           aux=0
           elif(i!=ent[0].get()+'\n' and aux==0):
               auxiliar.write(i)
       for c in range(4):
           for f in range(4):
               if(f!=3 or c==0):
                   botons[c][f].configure(state='normal')
       notas.close()
       auxiliar.close()
       notas=open('notas.dat.txt','w',encoding='utf-8')
       auxiliar=open('auxiliar.txt','r',encoding='utf-8')
       for c in auxiliar :
           notas.write(c)
       notas.close()
       auxiliar.close()
       alta_a.destroy()


def curso_mod(alta_a,event):
   for c in range(len(vec_aux2)):
       vec_aux2.pop()
   aux=int(0)
   cur=ent[0].get()+'°'+'\n'
   notas=open('notas.dat.txt','r',encoding='utf-8')
   for i in notas :
       if(i==cur or aux>0):
           aux+=1
           if(aux==2 or aux==3):
               vec_aux2.append(i)
               if(aux==3):
                   aux=0
   ent[1].configure(text=vec_aux2[0])
   ent[2].configure(text=vec_aux2[1])
   notas.close()


def modificar_not(alta_a):
  vec_aux=[]
  for i in range(len(texte)):
      texte.pop()
  for i in range(len(ent)):
      ent.pop()
  for elpepe in range(1,vec_id[1]):
      vec_aux.append(elpepe)
  for i in range(7):
      if(i==0):
          texte.append(Label(alta_a,text=id_n_a[i]+'a cambiar'))
      else:
          texte.append(Label(alta_a,text=id_n_a[i]))
      if(i==0):
          ent.append(ttk.Combobox(alta_a,state='readonly',values=vec_aux))
          ent[0].bind('<<ComboboxSelected>>',partial(curso_mod,alta_a))
      elif(i==1):
          ent.append(ttk.Label(alta_a,text='Falta Id_not'))
      elif(i==2):
          ent.append(ttk.Label(alta_a,text='Falta Id_not'))
      else:
          ent.append(Entry(alta_a))
  for j in range(7):
      texte[j].place(x=20,y=(30*j)+20,height=25,width=70)
      ent[j].place(x=100,y=(30*j)+20,height=25,width=200)


def modificar2(alta_a):
   auxi=int(0)
   for i in range(1,3):
      aux=ent[i].get()
      if(len(aux)<2 and auxi==0):
          auxi=1
          messagebox.showinfo(title='Error',message='Por lo menos coloca 2 caracteres')
   aux=int(0)
   if(auxi==0):
       materias=open('materias.dat.txt','r',encoding='utf-8')
       auxiliar=open('auxiliar.txt','w',encoding='utf-8')
       for i in materias :
           if(i==ent[0].get()+'\n' or aux>0):
               if(aux==0):
                   auxiliar.write(i)
                   aux=1
               else:
                   auxiliar.write(ent[aux].get()+'\n')
                   aux+=1
                   if(aux==3):
                       aux=0
           elif(i!=ent[0].get()+'\n' and aux==0):
               auxiliar.write(i)
       for c in range(4):
           for f in range(4):
               if(f!=3 or c==0):
                   botons[c][f].configure(state='normal')
       materias.close()
       auxiliar.close()
       materias=open('materias.dat.txt','w',encoding='utf-8')
       auxiliar=open('auxiliar.txt','r',encoding='utf-8')
       for c in auxiliar :
           materias.write(c)
       materias.close()
       auxiliar.close()
       alta_a.destroy()


def modificar(alta_a):
   auxi=int(0)
   for i in range(1,7):
      aux=ent[i].get()
      if(len(aux)<2 and auxi==0):
          auxi=1
          messagebox.showinfo(title='Error',message='Por lo menos coloca 2 caracteres')
   aux=int(0)
   if(auxi==0):
       alumnos=open('alumnos.dat.txt','r',encoding='utf-8')
       auxiliar=open('auxiliar.txt','w',encoding='utf-8')
       for i in alumnos :
           if(i==ent[0].get()+'\n' or aux>0):
               if(aux==0):
                   auxiliar.write(i)
                   aux=1
               else:
                   auxiliar.write(ent[aux].get()+'\n')
                   aux+=1
                   if(aux==7):
                       aux=0
           elif(i!=ent[0].get()+'\n' and aux==0):
               auxiliar.write(i)
       for c in range(4):
           for f in range(4):
               if(f!=3 or c==0):
                   botons[c][f].configure(state='normal')
       alumnos.close()
       auxiliar.close()
       alumnos=open('alumnos.dat.txt','w',encoding='utf-8')
       auxiliar=open('auxiliar.txt','r',encoding='utf-8')
       for c in auxiliar :
           alumnos.write(c)
       alumnos.close()
       auxiliar.close()
       alta_a.destroy()


def modificar_mat(alta_a):
  vec_aux=[]
  for i in range(len(texte)):
      texte.pop()
  for i in range(len(ent)):
      ent.pop()
  for elpepe in range(1,vec_id[2]):
      vec_aux.append(elpepe)
  for i in range(3):
      if(i==0):
          texte.append(Label(alta_a,text=id_m_a[i]+'a cambiar'))
      else:
          texte.append(Label(alta_a,text=id_m_a[i]))
      if(i==0):
          ent.append(ttk.Combobox(alta_a,state='readonly',values=vec_aux))
      elif(i==2):
          ent.append(ttk.Combobox(alta_a,state='readonly',values=cursos))
      else:
          ent.append(Entry(alta_a))
  for j in range(3):
      texte[j].place(x=20,y=(30*j)+20,height=25,width=70)
      ent[j].place(x=100,y=(30*j)+20,height=25,width=200) 


def modificar_alu(alta_a):
  vec_aux=[]
  for i in range(len(texte)):
      texte.pop()
  for i in range(len(ent)):
      ent.pop()
  for elpepe in range(1,vec_id[0]):
      vec_aux.append(elpepe)
  for i in range(7):
      if(i==0):
          texte.append(Label(alta_a,text=id_a_a[i]+'a cambiar'))
      else:
          texte.append(Label(alta_a,text=id_a_a[i]))
      if(i==0):
          ent.append(ttk.Combobox(alta_a,state='readonly',values=vec_aux))
      elif(i==5):
          ent.append(ttk.Combobox(alta_a,state='readonly',values=cursos))
      elif(i==6):
          ent.append(ttk.Combobox(alta_a,state='readonly',values=divis))
      else:
          ent.append(Entry(alta_a))
  for j in range(7):
      texte[j].place(x=20,y=(30*j)+20,height=25,width=70)
      ent[j].place(x=100,y=(30*j)+20,height=25,width=200)


def listado_m(alta_a,i):
   materias=open('materias.dat.txt','r',encoding='utf-8')
   auxiliar=open('auxiliar.txt','w',encoding='utf-8')
   auxili=int(0)
   for c in materias :
       b=c[:-1]
       auxiliar.write(b+',')
       auxili+=1
       if(auxili==3):
           auxili=0
           auxiliar.write('\n')
   auxiliar.close()
   materias.close()
   auxiliar=open('auxiliar.txt','r',encoding='utf-8')
   Frames=Frame(alta_a)
   Frames.pack(pady=10)
   Scroll=Scrollbar(Frames)
   Scroll.pack(side=RIGHT, fill=Y)
   Tree=ttk.Treeview(Frames, columns=(1,2,3), show="headings", yscrollcommand=Scroll.set, selectmode="extended")
   Tree.tag_configure('Gray', background='White')
   for h in range(4):
       Tree.heading(h,text=id_m_a[h-1])
   Scroll.config(command=Tree.yview)
   reader_c=int(0)
   reader=auxiliar.readline()[:-1]
   while(reader != ''):
       if(reader_c%2==0):
           print('a')
           Tree.insert('','end',values=reader.split(',',6),)
       else:
           Tree.insert('','end',values=reader.split(',',6),tag='Gray')
       reader_c+=1
       reader= auxiliar.readline()[:-1]
   Tree.pack()
   Tree.focus_set()
   auxiliar.close()


def listado_n(alta_a,i):
   notas=open('notas.dat.txt','r',encoding='utf-8')
   auxiliar=open('auxiliar.txt','w',encoding='utf-8')
   auxili=int(0)
   for c in notas :
       b=c[:-1]
       auxiliar.write(b+',')
       auxili+=1
       if(auxili==7):
           auxili=0
           auxiliar.write('\n')
   auxiliar.close()
   notas.close()
   auxiliar=open('auxiliar.txt','r',encoding='utf-8')
   Frames=Frame(alta_a)
   Frames.pack(pady=10)
   Scroll=Scrollbar(Frames)
   Scroll.pack(side=RIGHT, fill=Y)
   Tree=ttk.Treeview(Frames, columns=(1,2,3,4,5,6,7), show="headings", yscrollcommand=Scroll.set, selectmode="extended")
   Tree.tag_configure('Gray', background='White')
   for h in range(8):
       Tree.heading(h,text=id_n_a[h-1])
   Scroll.config(command=Tree.yview)
   reader_c=int(0)
   reader=auxiliar.readline()[:-1]
   while(reader != ''):
       if(reader_c%2==0):
           print('a')
           Tree.insert('','end',values=reader.split(',',6),)
       else:
           Tree.insert('','end',values=reader.split(',',6),tag='Gray')
       reader_c+=1
       reader= auxiliar.readline()[:-1]
   Tree.pack()
   Tree.focus_set()
   auxiliar.close()


def listado_a(alta_a,i):
   alumnos=open('alumnos.dat.txt','r',encoding='utf-8')
   auxiliar=open('auxiliar.txt','w',encoding='utf-8')
   auxili=int(0)
   for c in alumnos :
       b=c[:-1]
       auxiliar.write(b+',')
       auxili+=1
       if(auxili==7):
           auxili=0
           auxiliar.write('\n')
   auxiliar.close()
   alumnos.close()
   auxiliar=open('auxiliar.txt','r',encoding='utf-8')
   Frames=Frame(alta_a)
   Frames.pack(pady=10)
   Scroll=Scrollbar(Frames)
   Scroll.pack(side=RIGHT, fill=Y)
   Tree=ttk.Treeview(Frames, columns=(1,2,3,4,5,6,7), show="headings", yscrollcommand=Scroll.set, selectmode="extended")
   Tree.tag_configure('Gray', background='White')
   for h in range(8):
       Tree.heading(h,text=id_a_a[h-1])
   Scroll.config(command=Tree.yview)
   reader_c=int(0)
   reader=auxiliar.readline()[:-1]
   while(reader != ''):
       if(reader_c%2==0):
           print('a')
           Tree.insert('','end',values=reader.split(',',6),)
       else:
           Tree.insert('','end',values=reader.split(',',6),tag='Gray')
       reader_c+=1
       reader= auxiliar.readline()[:-1]
   Tree.pack()
   Tree.focus_set()
   auxiliar.close()

def listado_boletines(alta_a,cb):
   alumnos=open('alumnos.dat.txt','r',encoding='utf-8')
   auxiliar=open('auxiliar2.txt','w',encoding='utf-8')
   auxili=int(0)
   aux=int(0)
   aux2=''
   for c in alumnos :
       if(cb+'\n'==c or aux>0):
           if(cb+'\n'==c):
               qwerty=c[:-1]
               auxiliar.write(qwerty+',')
               aux=6
           else:
               qwerty=c[:-1]
               auxiliar.write(qwerty+',')
               aux-=1
   auxiliar.write('\n')
   aux=0
   alumnos.close()
   alumnos=open('alumnos.dat.txt','r',encoding='utf-8')   
   for c in alumnos :
      if(cb+'\n'==c or aux>0):
         aux+=1
         if(aux==6):
            aux2=c
            aux=0
   aux=0
   auxl=int(0)
   auxll=int(0)
   materias=open('materias.dat.txt','r',encoding='utf-8')
   for c in materias :
       if(c==aux2):
           qwe=auxl[:-1]
           qwer=auxll[:-1]
           qwert=c[:-1]
           auxiliar.write(qwe+',')
           auxiliar.write(qwer+',')
           auxiliar.write(qwert+',')
           auxiliar.write('\n')
       auxl=auxll
       auxll=c

   aux=0
   auxl=0
   auxll=-1
   auxlll=int(0)
   notas=open('notas.dat.txt','r',encoding='utf-8')
   for c in notas :
       auxll+=1
       print(cb,'-',c)
       if((c==cb+'\n' and (auxll-1)%7==0) or aux>0):
           if(c==cb+'\n'):
               qwe=auxl[:-1]
               qwer=c[:-1]
               auxiliar.write(qwe+',')
               auxiliar.write(qwer+',')
               auxlll+=2
               aux=5
               print(qwe,qwer)
           else:
               qwer=c[:-1]
               auxiliar.write(qwer+',')
               auxlll+=1
               print('|'+qwer)
               aux-=1
       if(auxlll==7):
           auxlll=0
           auxiliar.write('\n')
       auxl=c

   auxiliar.close()
   materias.close()
   notas.close()
   alumnos.close()
   
   auxiliar=open('auxiliar2.txt','r',encoding='utf-8')
   Frames=Frame(alta_a)
   Frames.pack(pady=10)
   Scroll=Scrollbar(Frames)
   Scroll.pack(side=RIGHT, fill=Y)
   Tree=ttk.Treeview(Frames, columns=(1,2,3,4,5,6,7), show="headings", yscrollcommand=Scroll.set, selectmode="extended")
   Tree.tag_configure('Gray', background='White')
   Scroll.config(command=Tree.yview)
   reader_c=int(0)
   reader=auxiliar.readline()[:-1]
   while(reader != ''):
       if(reader_c%2==0):
           print('a')
           Tree.insert('','end',values=reader.split(',',6),)
       else:
           Tree.insert('','end',values=reader.split(',',6),tag='Gray')
       reader_c+=1
       reader= auxiliar.readline()[:-1]
   Tree.pack()
   Tree.focus_set()
   auxiliar.close()
   print('eeeeeeea')

def baja_nota(alta_a):
   for i in range(len(texte)):
       texte.pop()
   for i in range(len(ent)):
       ent.pop()
   texte.append(Label(alta_a,text='id not a Borrar'))
   nums3=idedes(1)
   ent.append(ttk.Combobox(alta_a,state='readonly',values=nums3))
   texte[0].place(x=20,y=20,height=25,width=90)
   ent[0].place(x=110,y=20,height=25,width=200)


def baja_mat(alta_a):
  for i in range(len(texte)):
      texte.pop()
  for i in range(len(ent)):
      ent.pop()
  texte.append(Label(alta_a,text='id mat a Borrar'))
  nums2=idedes(2)
  ent.append(ttk.Combobox(alta_a,state='readonly',values=nums2))
  texte[0].place(x=20,y=20,height=25,width=90)
  ent[0].place(x=110,y=20,height=25,width=200)


def borrar3(alta_a):
   if(ent[0].get()!=''):
       aux=int(0)
       notas=open('notas.dat.txt','r',encoding='utf-8')
       auxiliar=open('auxiliar.txt','w',encoding='utf-8')
       for c in notas :
           if(c!=ent[0].get()+'°'+'\n' and aux==0):
               auxiliar.write(c)
           else:
               if(c==ent[0].get()+'°'+'\n'):
                   cb=c[:-1]
                   vec_n_bor.append(cb)
                   borran=open('borra_n.dat.txt','a',encoding='utf-8')
                   borran.write(cb+'\n')
                   borran.close()
                   aux=6
               else:
                   aux-=1
       for c in range(4):
           for f in range(4):
               if(f!=3 or c==0):
                   botons[c][f].configure(state='normal')
       notas.close()
       auxiliar.close()
       notas=open('notas.dat.txt','w',encoding='utf-8')
       auxiliar=open('auxiliar.txt','r',encoding='utf-8')
       for c in auxiliar :
           notas.write(c)
       notas.close()
       auxiliar.close()
       alta_a.destroy()
   else:
       messagebox.showinfo(title='Error',message='Selecciona un dato')
      




def borrar2(alta_a):
  if(ent[0].get()!=''):
      aux=int(0)
      materias=open('materias.dat.txt','r',encoding='utf-8')
      auxiliar=open('auxiliar.txt','w',encoding='utf-8')
      for c in materias :
          if(c!=ent[0].get()+'\n' and aux==0):
              auxiliar.write(c)
          else:
              if(c==ent[0].get()+'\n'):
                  cb=c[:-1]
                  vec_m_bor.append(int(cb))
                  borram=open('borra_m.dat.txt','a',encoding='utf-8')
                  borram.write(cb+'\n')
                  borram.close()
                  aux=2
              else:
                  aux-=1
                 
      for c in range(4):
          for f in range(4):
              if(f!=3 or c==0):
                  botons[c][f].configure(state='normal')


      materias.close()
      auxiliar.close()
      materias=open('materias.dat.txt','w',encoding='utf-8')
      auxiliar=open('auxiliar.txt','r',encoding='utf-8')
      for c in auxiliar :
          materias.write(c)
      materias.close()
      auxiliar.close()
      alta_a.destroy()
  else:
      messagebox.showinfo(title='Error',message='Selecciona un dato')




def baja_alum(alta_a):
  for i in range(len(texte)):
      texte.pop()
  for i in range(len(ent)):
      ent.pop()
  texte.append(Label(alta_a,text='id alu a Borrar'))
  nums=idedes(0)
  ent.append(ttk.Combobox(alta_a,state='readonly',values=nums))
  texte[0].place(x=20,y=20,height=25,width=90)
  ent[0].place(x=110,y=20,height=25,width=200)




def borrar(alta_a):
  if(ent[0].get()!=''):
      aux=int(0)
      alumno=open('alumnos.dat.txt','r',encoding='utf-8')
      auxiliar=open('auxiliar.txt','w',encoding='utf-8')
      for c in alumno :
          if(c!=ent[0].get()+'\n' and aux==0):
              auxiliar.write(c)
          else:
              if(c==ent[0].get()+'\n'):
                  cb=c[:-1]
                  vec_a_bor.append(int(cb))
                  borraa=open('borra_a.dat.txt','a',encoding='utf-8')
                  borraa.write(cb+'\n')
                  borraa.close()
                  aux=6
              else:
                  aux-=1


      for c in range(4):
          for f in range(4):
              if(f!=3 or c==0):
                  botons[c][f].configure(state='normal')
      
      alumno.close()
      auxiliar.close()
      alumno=open('alumnos.dat.txt','w',encoding='utf-8')
      auxiliar=open('auxiliar.txt','r',encoding='utf-8')
      for c in auxiliar :
          alumno.write(c)
      alumno.close()
      auxiliar.close()
      alta_a.destroy()
  else:
      messagebox.showinfo(title='Error',message='Selecciona un dato')

def idedes3(i):
    m=[]
    for c in range(1,vec_id[i]):
        m.append(str(c))
    return(m)
    
def idedes(i):
  m=[]
  for c in range(1,vec_id[i]):
      if(i==0):
          aux=int(0)
          for j in range(len(vec_a_bor)):
             if(c==vec_a_bor[j]):
                 aux+=1
          if(aux==0):
             m.append(str(c))
      elif(i==1):
          aux=int(0)
          for j in range(len(vec_n_bor)):
              if(c==vec_n_bor[j]):
                  aux+=1
          if(aux==0):
              m.append(str(c))
      elif(i==2):
          aux=int(0)
          for j in range(len(vec_m_bor)):
             if(c==vec_m_bor[j]):
                 aux+=1
          if(aux==0):
             m.append(str(c))
  return(m)


def idedes2(b):
   m=[]
   for c in range(0,vec_id[2]-1):
       if(curso_sel[b-1]==curso_disp[c]):
           m.append(str(c+1))
   return(m)




def alta_mat(alta_a):
  for i in range(len(texte)):
      texte.pop()
  for i in range(len(ent)):
      ent.pop()
  for i in range(3):
      texte.append(Label(alta_a,text=id_m_a[i]))
      if(i==0):
          ent.append(Label(alta_a,text=str(vec_id[2])))
      elif(i==1):
          ent.append(Entry(alta_a))
      else:
          ent.append(ttk.Combobox(alta_a,state='readonly',values=cursos))
  for j in range(3):
      texte[j].place(x=20,y=(30*j)+20,height=25,width=70)
      ent[j].place(x=100,y=(30*j)+20,height=25,width=200)


def alta_nota(alta_a):
  for i in range(len(texte)):
      texte.pop()
  for i in range(len(ent)):
      ent.pop()
  for i in range(7):
      texte.append(Label(alta_a,text=id_n_a[i]))
      if(i==0):
          ent.append(Label(alta_a,text=str(vec_id[1])))
      elif(i==1):
          idalu=idedes3(0)
          ent.append(ttk.Combobox(alta_a,state='readonly',values=idalu))
          ent[i].bind('<<ComboboxSelected>>',partial(curso_alumno,alta_a))
      elif(i==2):
          ent.append(ttk.Combobox(alta_a,state='disable',values=falso_idmat))
      else:
          ent.append(Entry(alta_a))
  for j in range(7):
      texte[j].place(x=20,y=(30*j)+20,height=25,width=70)
      ent[j].place(x=100,y=(30*j)+20,height=25,width=200)




def curso_alumno(alta_a,event):
   a=event.widget
   print('e')
   b=int(ent[1].get())
   idmat=idedes2(b)
   ent[2].configure(state='readonly',values=idmat)


def alta_alum(alta_a):
  for i in range(len(texte)):
      texte.pop()
  for i in range(len(ent)):
      ent.pop()
  for i in range(7):
      texte.append(Label(alta_a,text=id_a_a[i]))
      if(i==0):
          ent.append(Label(alta_a,text=str(vec_id[0])))
      elif(i==5):
          ent.append(ttk.Combobox(alta_a,state='readonly',values=cursos))
      elif(i==6):
          ent.append(ttk.Combobox(alta_a,state='readonly',values=divis))
      else:
          ent.append(Entry(alta_a))
  for j in range(7):
      texte[j].place(x=20,y=(30*j)+20,height=25,width=70)
      ent[j].place(x=100,y=(30*j)+20,height=25,width=200)




def cerrar(l,i):
  for c in range(4):
      for f in range(4):
          if(f!=3 or c==0):
              botons[c][f].configure(state='normal')
  l.destroy()


def agregar3(alta_a):
   auxi=int(0)
   for i in range(1,7):
       aux=ent[i].get()
       if(len(aux)<1 and auxi==0):
           auxi=1
           messagebox.showinfo(title='Error',message='Por lo menos coloca 2 caracteres')
   if(auxi==0):
       notas=open('notas.dat.txt','a',encoding='utf-8')
       for i in range(7):
           if(i>0):
               aux=ent[i].get()
               notas.write(str(aux)+'\n')
           else:
               notas.write(str(vec_id[1])+'°'+'\n')
       for c in range(4):
           for f in range(4):
               if(f!=3 or c==0):
                   botons[c][f].configure(state='normal')
       vec_id[1]+=1
       id_n=open('id_n.dat.txt','w',encoding='utf-8')
       id_n.write(str(vec_id[1]))
       id_n.close()
       ventana.update()
       alta_a.destroy()
       notas.close()       


def agregar2(alta_a):
   auxi=int(0)
   for i in range(1,3):
       aux=ent[i].get()
       if(len(aux)<2 and auxi==0):
           auxi=int(1)
           messagebox.showinfo(title='Error',message='Por lo menos coloca 2 caracteres')
   if(auxi==0):
       materias=open('materias.dat.txt','a',encoding='utf-8')
       for i in range(3):
           if(i>0):
               aux=ent[i].get()
               materias.write(str(aux)+'\n')
           else:
               materias.write(str(vec_id[2])+'\n')
           if(i==2):
               curso_m=open('curso_m.dat.txt','a',encoding='utf-8')
               curso_m.write(ent[2].get()+'\n')
               curso_disp.append(ent[2].get()+'\n')
               curso_m.close()
       for c in range(4):
           for f in range(4):
               if(f!=3 or c==0):
                   botons[c][f].configure(state='normal')
       vec_id[2]+=1
       id_m=open('id_m.dat.txt','w',encoding='utf-8')
       id_m.write(str(vec_id[2]))
       id_m.close()
       ventana.update()
       alta_a.destroy()
       materias.close()

def corrobora(alta_a,cb):
    aux=int(-1)
    aux2=int(0)
    aux3=int(0)
    aux4=int(0)
    for i in cb :
        aux+=1
        if((i=='@' or i=='.') and aux==len(cb)-1):
            return(False)
        if((i=='@' or i=='.') and aux==0):
            return(False)
        if(i=='@' or aux2>0):
            aux2+=1
            if(i=='.' and aux2==2):
                return(False)
            if(i=='.'):
                aux3=1
    for i in cb :
        if(i=='@'):
            aux4+=1
    if(aux3==1 and aux4==1):
        return(True)
    else:
        return(False)


def agregar(alta_a):
  auxi=int(0)
  aux3=int(0)
  for i in range(1,7):
      aux=ent[i].get()
      if(len(aux)<2 and auxi==0):
          auxi=1
          messagebox.showinfo(title='Error',message='Por lo menos coloca 2 caracteres')
  if(auxi==0):
      alumnos=open('alumnos.dat.txt','a',encoding='utf-8')
      for i in range(7):
          if(i>0 and i!=4):
              aux=ent[i].get()
              alumnos.write(str(aux)+'\n')
          elif(i==0):
              alumnos.write(str(vec_id[0])+'\n')
          elif(i==4):
              cb=ent[4].get()
              aux2=corrobora(alta_a,cb)
              if(aux2==False):
                  messagebox.showinfo(title='Error',message='Necesitas poner una sola @ y minimo un "." no adyacente a esta, que esté despues de la misma y que no esten ni al final ni al principie')
                  aux3=1
              elif(aux2==True):
                  aux=ent[i].get()
                  alumnos.write(str(aux)+'\n')
          if(i==5):
              curso_a=open('curso_a.dat.txt','a',encoding='utf-8')
              curso_a.write(ent[5].get()+'\n')
              curso_sel.append(ent[5].get()+'\n')
              curso_a.close()
      if(aux3==0):
          for c in range(4):
              for f in range(4):
                  if(f!=3 or c==0):
                      botons[c][f].configure(state='normal')
          vec_id[0]=vec_id[0]+1          
          id_a=open('id_a.dat.txt','w',encoding='utf-8')
          id_a.write(str(vec_id[0]))
          id_a.close()
          ventana.update()
          alta_a.destroy()
          alumnos.close()

borraa=open('borra_a.dat.txt','a',encoding='utf-8')
borram=open('borra_m.dat.txt','a',encoding='utf-8')
borran=open('borra_n.dat.txt','a',encoding='utf-8')
curso_a=open('curso_a.dat.txt','a',encoding='utf-8')
curso_m=open('curso_m.dat.txt','a',encoding='utf-8')
alumnos=open('alumnos.dat.txt','a',encoding='utf-8')
notas=open('notas.dat.txt','a',encoding='utf-8')
materias=open('materias.dat.txt','a',encoding='utf-8')
id_a=open('id_a.dat.txt','a',encoding='utf-8')
id_n=open('id_n.dat.txt','a',encoding='utf-8')
id_m=open('id_m.dat.txt','a',encoding='utf-8')
id_a.close()
id_m.close()
id_n.close()
id_a=open('id_a.dat.txt','r',encoding='utf-8')
id_n=open('id_n.dat.txt','r',encoding='utf-8')
id_m=open('id_m.dat.txt','r',encoding='utf-8')
auxiliar=open('auxiliar.txt','w',encoding='utf-8')
auxiliar.close()
auxiliar=open('auxiliar.txt','r',encoding='utf-8')
auxiliar2=open('auxiliar2.txt','w',encoding='utf-8')
d=auxiliar.read()
a=id_a.read()
b=id_m.read()
c=id_n.read()
id_a.close()
id_m.close()
id_n.close()
borraa.close()
borram.close()
borran.close()
id_a=open('id_a.dat.txt','a',encoding='utf-8')
id_n=open('id_n.dat.txt','a',encoding='utf-8')
id_m=open('id_m.dat.txt','a',encoding='utf-8')
print(a,b,c,d)
if(a == d and b == d and c == d):
   id_a.write(str(1))
   id_m.write(str(1))
   id_n.write(str(1))
auxiliar.close()
auxiliar2.close()
alumnos.close()
notas.close()
materias.close()
id_a.close()
id_n.close()
id_m.close()
curso_a.close()
curso_m.close()


id_a=open('id_a.dat.txt','r',encoding='utf-8')
id_n=open('id_n.dat.txt','r',encoding='utf-8')
id_m=open('id_m.dat.txt','r',encoding='utf-8')
vec_id=[0,0,0]
vec_id[0]=int(id_a.read())
vec_id[1]=int(id_n.read())
vec_id[2]=int(id_m.read())
          
ventana= Tk()
ventana.geometry('600x400+150+150')
ventana.title('Sistema de Gestión de Boletines')


cursos=['1°','2°','3°','4°','5°','6°']
falso_idmat=['Vacio']
curso_sel=[]
curso_disp=[]


curso_a=open('curso_a.dat.txt','r',encoding='utf-8')
curso_m=open('curso_m.dat.txt','r',encoding='utf-8')
for c in range(len(curso_sel)):
   curso_sel.pop
for c in range(len(curso_disp)):
   curso_disp.pop
  
for i in curso_a :
   curso_sel.append(i)
for i in curso_m :
   curso_disp.append(i)


curso_a.close()
curso_m.close()

vec_a_bor=[]
vec_m_bor=[]
vec_n_bor=[]

divis=['1°','2°','3°','4°','5°']
nom_l=['Alumnos','Notas','Materias','Boletines']
nom_b=['Alta','Baja','Modificaciones','Listados']
id_a_a=['id_alu','DNI','Apellido','Nombre','Email','Curso','División']
id_m_a=['id_mat','Nombre','Curso']
id_n_a=['id_not','id_alu','id_mat','Nota 1','Nota 2','Nota 3','Nota 4']

borraa=open('borra_a.dat.txt','r',encoding='utf-8')
borram=open('borra_m.dat.txt','r',encoding='utf-8')
borran=open('borra_n.dat.txt','r',encoding='utf-8')
for c in borraa :
    vec_a_bor.append(c)
for c in borram :
    vec_m_bor.append(c)
for c in borran :
    vec_n_bor.append(c)
borraa.close()
borram.close()
borran.close()
labels=[]
texte=[]
vec_aux2=[]
ent=[]


vectombo=[None,None]
botons=cargar()


labeles()
botones()


ventana.mainloop()
