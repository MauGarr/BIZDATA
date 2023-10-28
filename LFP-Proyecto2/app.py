from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.font import families

#Root
ventana = Tk()
ventana.config(background="#044D9A")

ventana.geometry("1200x900")
ventana.title("Editor de base de datos")

#Ventana de edicion y lectura de texto
textoEntrada = Text(ventana, height=40, width=70, bg="#313131", fg="white", font=("Consolas", 11)) 
textoEntrada.place(x=10, y=100)


textoSalida = Text(ventana, height=40, width=70, bg="#313131",state='disabled', fg="white", font=("Consolas", 11))
textoSalida.place(x=600, y=100)


#Botones
btnAbrirArchivo = Button(ventana, height=2, width=10, text="Abrir archivo", command = , background="#368807", font=("Verdana",10), fg="white")
btnAbrirArchivo.place(x=320, y=50)

btnAnalizar = Button(ventana, height=2, width=10, text="Compilar", command=, background="#10139E", font=("Verdana",10), fg="white")
btnAnalizar.place(x=420, y=50)

btnReporeteTokensValidos = Button(ventana, height=2, width=12, text="Tokens válidos",command=, background="#8E8C08", font=("Verdana",10), fg="white")
btnReporeteTokensValidos.place(x=515, y=50)

btnReporeteTokensInvalidos = Button(ventana, height=2, width=13, text="Errores",command=, background="#B03314", font=("Verdana",10), fg="white")
btnReporeteTokensInvalidos.place(x=630, y=50)

btnReporeteGrpahviz = Button(ventana, height=2, width=10, text="Graphviz" , command=, background="#0D9597", font=("Verdana",10), fg="white")
btnReporeteGrpahviz.place(x=750, y=50)

#Labels
labelEditor = Label (ventana, text ="EDITOR DE TEXTO", font=("Verdana",15), background="#044D9A", fg="white")
labelEditor.place(x=90, y=50)

labelTerminal = Label (ventana, text ="TERMINAL", font=("Verdana",15), background="#044D9A", fg="white")
labelTerminal.place(x=900, y=50)

ventana.mainloop()