#!/usr/bin/env python
#-*- coding:utf8 -*-
from Tkinter import *
import tkMessageBox

#----------------------------------------------------------------------------------------------------
'''   					CREACION DE LA VENTANA PRINCIPAL                                           '''
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
ventana = Tk()


ventana.title("Convertir palabra")
ventana.config(bg="#1F6095")
ventana.geometry("820x350+340+150")
ventana.resizable(0,0)
#ventana.centerWindow()

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------




#----------------------------------------------------------------------------------------------------
'''         					ADAPTACION DE LA VENTANA PRINCIPAL                               '''
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
imagenHCK = PhotoImage(file='./hck1.gif')
labHCK = Label(ventana,image=imagenHCK,relief=FLAT)
labHCK.place(x=700,y=43)


topLabel = Label(ventana, text="PiR00d Haslam",bg="#1F6095",font='{courier 200 bold}',justify="center")
topLabel.place(x=300,y=5)

wordEntry = StringVar()
wordAscii = StringVar()
wordHex = StringVar()
wordBin = StringVar()


labelInWord = Label(ventana,text="Introdusca la palabra: ",relief="flat",bg="#1F6095",font='{courier 200 bold}')
labelInWord.place(x=240,y=40)

entradaWord = Entry(ventana,textvar=wordEntry,relief=FLAT)
entradaWord.place(x=240,y=80)

# Etiqueta ascii
labelAscii = Label(ventana,text="Ascii: ",bg="#1F6095",font='{courier 200 bold}')
labelAscii.place(x=20,y=140)
# Muestra valor de la palabra en Ascii en una etiqueta
labelOutAscii = Label(ventana,textvar=wordAscii,bg="#1F6095",font='{courier 200 bold}')
labelOutAscii.place(x=70,y=140)
# Boton de copiar palabra en Ascii
copyWordAscii = Button(ventana,text="Copy",relief=FLAT,border=2,command=lambda:copy2clip(cadenaHex))
copyWordAscii.place(x=20,y=160)

labelHex = Label(ventana,text="Hex: ",bg="#1F6095",font='{courier 200 bold}')
labelHex.place(x=20,y=220)
labelOutHex = Label(ventana,textvar=wordHex,bg="#1F6095",font='{courier 200 bold}')
labelOutHex.place(x=70,y=220)

labelBin = Label(ventana,text="Bin: ",bg="#1F6095",font='{courier 200 bold}')
labelBin.place(x=20,y=250)
labelOutBin = Label(ventana,textvar=wordBin,bg="#1F6095",font='{courier 200 bold}')
labelOutBin.place(x=70,y=250)


botonGenerar = Button(ventana,text="Generar",relief=FLAT,command=lambda:obtenerAscii(wordEntry.get(),wordAscii))
botonGenerar.place(x=420,y=75)

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------
'''   					CREACION DEL SPLASH PRINCIPAL                                              '''
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

v1=Toplevel(ventana)
v1.geometry("500x500+420+100")
v1.config(bg="white")
v1.protocol("WM_DELETE_WINDOW", "onexit")
v1.resizable(0,0)

dogSir = PhotoImage(file="./dogLikeSir.gif")
imagenHCK1 = PhotoImage(file='./hck2.gif')
labHCKSplash = Label(v1,image=imagenHCK1,relief=FLAT)
labHCKSplash.place(x=400,y=20)


def imprimir(texto): print texto
def mostrar(ventana): return ventana.deiconify # Muestra una ventana
def ocultar(ventana): return ventana.withdraw() # Oculta una ventana
def ejecutar(f): ventana.after(100, f)

ocultar(ventana)
def cerrar_splashscreen():
    ejecutar(ocultar(v1))
    ejecutar(mostrar(ventana))
v1.after(4000,cerrar_splashscreen)
labelShowTextSplash = Label(v1,text="PiR00d Haslam",relief=FLAT,bg="white",fg="black",font='{courier 200 bold}')
labelShowTextSplash.place(x=120,y=15)
labelShowImgSplash = Label(v1,image=dogSir,relief=FLAT,bg="white",font='{courier 200 bold}',justify="center")
labelShowImgSplash.place(x=90,y=90)

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------
'''   					FUCNIONES  A EJECUTAR                                                     '''
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
listadeCadenasAscii = []

#def mostrarPalabra(palabraIn,showWord):
#	showWord.set("["+palabraIn+"]")

cadenaAscii = ""
cadenaHex = ""
cadenaBin = ""

def obtenerAscii(palabra,showAscii):
	listadeCadenasAscii = []
	variable = palabra
	global cadenaAscii
	tamVariable = len(variable)
	# Obtener el ASCII de una palabra (Completo)
	for i in range(tamVariable):
		auxVar = variable[i]
		auxVar = ord(auxVar)
		auxVar = str(auxVar)
		cadenaAscii = cadenaAscii + auxVar
		listadeCadenasAscii.insert(i,auxVar)
	showAscii.set("["+cadenaAscii+"]")
	obtenerHex(listadeCadenasAscii,wordHex)
	obtenerBinario(listadeCadenasAscii,wordBin)

def obtenerHex(palabra,showHex):
	listaAscii = palabra
	listadeCadenasHex = []
	global cadenaHex
	for j in range(0,len(listaAscii)):
		varToHex = listaAscii[j]
		varToHex = int(varToHex)
		varHex = hex(varToHex)
		varHex = str(varHex)
		varHex = varHex[2:]
		cadenaHex = cadenaHex + varHex
	showHex.set("["+cadenaHex+"]")


def obtenerBinario(palabra,showBin):
	listaAsciiB = palabra
	global cadenaBin
	for k in range(0,len(listaAsciiB)):
		varToBin = listaAsciiB[k]
		varToBin = int(varToBin)
		varBin = bin(varToBin)
		varBin = str(varBin)
		varBin = varBin[2:]
		cadenaBin = cadenaBin + varBin
	showBin.set("["+cadenaBin+"]")

def copy2clip(word):
	v1.clipboard_clear()
	v1.clipboard_append(word)
	clipText = v1.clipboard_get()
	global cadenaHex
	print "Cadena copiada correctamente! :%s" %cadenaHex

ventana.mainloop()
