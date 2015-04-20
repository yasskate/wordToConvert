#!/usr/bin/env python
#-*- coding:utf8 -*-
from Tkinter import *

v0=Tk()
v0.geometry("500x500")

imagen1=PhotoImage(file="/root/Desktop/wordToConvert/hck1.gif")

imagen2 = PhotoImage(file="/root/Desktop/wordToConvert/dogLikeSir.gif")
label2 = Label(v0,image=imagen2).pack()

def imprimir(texto): print texto
def mostrar(ventana): return ventana.deiconify # Muestra una ventana
def ocultar(ventana): return ventana.withdraw() # Oculta una ventana
def ejecutar(f): v0.after(100, f)

v1=Toplevel(v0)
v1.geometry("400x200")
v1.config(bg="black")
v1.protocol("WM_DELETE_WINDOW", "onexit")
v1.resizable(0,0)

ocultar(v0)
def cerrar_splashscreen():
    ejecutar(ocultar(v1))
    ejecutar(mostrar(v0))
v1.after(4000,cerrar_splashscreen)
Label(v1,text="BIENVENIDO A NUESTRA APLICACIÓN",bg="black",fg="white",font=(15)).pack()
Label(v1,image=imagen1).pack()


v0.mainloop()