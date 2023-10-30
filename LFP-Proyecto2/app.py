from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter.font import families
from Analizador import Analizador

analizador = Analizador()

# - - - Funciones - - - #

def reporteTokens():
    analizador.reporteTokensValidos()

def reporteErrores():
    analizador.reportesErrores()
    analizador.erroresSintacticos.clear()

def abrirArchvo1():
    global archivo, textoLeido

    textoEntrada.delete('1.0', END)

    archivo = filedialog.askopenfilename(title="Abrir", filetypes=[("Archivo BIZDATA", "*.BIZDATA"), ("Archivo TXT", "*.txt")])
    archivos_texto = open(archivo, 'r', encoding='utf-8')
    textoLeido = archivos_texto.read()
    textoEntrada.insert(tk.END, textoLeido)

def Compilar():
    global textoObtenido

    textoObtenido = textoEntrada.get(1.0, tk.END+"-1c")

    print(textoObtenido)

    docLFP = open(archivo,"w", encoding='utf-8')
    docLFP.write(textoObtenido)
    docLFP.close()

    archivos_texto = open(archivo, 'r', encoding='utf-8')
    textoLeido = archivos_texto.read()
    analizador.scanner(textoLeido)
    analizador.imprimirTokens()
    analizador.imprimirErrores()
    
    textoSalida.configure(state='normal')
    textoSalida.delete('1.0', END)
    textoSalida.configure(state='disabled')

    boolimprimir = False
    boolimprimirln = False
    boolpromedio = False
    boolsuma = False
    boolmax = False
    boolmin = False
    boolcontarsi = False
    boolreporte = False
    nombre = ''
    salidaN = ''
    clave = ''
    numero = 0

    if analizador.generarErrores == False:
        analizador.Claves()
        analizador.Registros()
        analizador.SintacticoImprimirReporte()
        analizador.sintacticoConteoDatos()
        analizador.sintacticoPromMaxMinSum()
        analizador.sintacticoContarSi()

    if analizador.generarErrores == False:

        for i in analizador.tokens:

            #Imprimir cadena sin salto de linea
            if i.getLexema().lower() == 'imprimir':
                boolimprimir = True
            elif i.getTipo() == 'CADENA' and boolimprimir:
                salidaN = str(i.getLexema()) 
                textoSalida.configure(state='normal')
                textoSalida.insert(END, salidaN)
                textoSalida.configure(state='disabled')
            elif i.getTipo() == 'PUNTO Y COMA' and boolimprimir:
                salidaN = ''
                boolimprimir= False
            
            #Imprimir cadenas con salto de linea
            elif i.getLexema().lower() == 'imprimirln':
                boolimprimirln = True

            elif i.getTipo() == 'CADENA' and boolimprimirln:
                salidaLn = str(i.getLexema())+'\n'
                textoSalida.configure(state='normal')
                textoSalida.insert(END, salidaLn)
                textoSalida.configure(state='disabled')
            elif i.getTipo() == 'PUNTO Y COMA' and boolimprimirln:
                salidaLn = ''
                boolimprimirln = False
            
            #Opcion de mostar los datos
            elif i.getLexema().lower() == 'datos':
                
                for i in analizador.claves:
                    textoSalida.configure(state='normal')
                    textoSalida.insert(END, i+'   ')
                    textoSalida.configure(state='disabled')
                
                #Crear un salto de linea
                textoSalida.configure(state='normal')
                textoSalida.insert(END,'\n')
                textoSalida.configure(state='disabled')
                cont = 0

                for j in analizador.registros:
                    if cont != len(analizador.claves):
                        textoSalida.configure(state='normal')
                        textoSalida.insert(END, j.getRegistro()+'       ')
                        textoSalida.configure(state='disabled')
                    else:
                        textoSalida.configure(state='normal')
                        textoSalida.insert(END,'\n' + j.getRegistro()+ '        ')
                        textoSalida.configure(state='disabled')
                        cont = 0
                    cont += 1
                
                textoSalida.configure(state='normal')
                textoSalida.insert(END,'\n')
                textoSalida.configure(state='disabled')
            
            #Promedio
            elif i.getLexema().lower()=='promedio':
                boolpromedio = True
            
            elif i.getTipo() == 'CADENA' and boolpromedio:
                clave = i.getLexema()
                
                textoSalida.configure(state='normal')
                textoSalida.insert(END, analizador.Promedio(clave) + '\n')
                textoSalida.configure(state='disabled')

                clave = ''
                boolpromedio = False

            #Conteo
            elif i.getLexema().lower() == 'conteo':
                datosTotales = (len(analizador.registros)) / (len(analizador.claves))
                
                textoSalida.configure(state='normal')
                textoSalida.insert(END,str(datosTotales) +'\n')
                textoSalida.configure(state='disabled')
            
            #Suma de un campo
            elif i.getLexema().lower()=='sumar':
                boolsuma = True
            
            elif i.getTipo() == 'CADENA' and boolsuma:
                clave = i.getLexema()
                
                textoSalida.configure(state='normal')
                textoSalida.insert(END, analizador.Sumar(clave) + '\n')
                textoSalida.configure(state='disabled')

                clave = ''
                boolsuma = False
            
            #Maximo
            elif i.getLexema().lower()=='max':
                boolmax = True
            
            elif i.getTipo() == 'CADENA' and boolmax:
                clave = i.getLexema()
                
                textoSalida.configure(state='normal')
                textoSalida.insert(END, analizador.Maximo(clave) + '\n')
                textoSalida.configure(state='disabled')

                clave = ''
                boolmax = False
            
            #Minimo
            elif i.getLexema().lower()=='min':
                boolmin = True
            
            elif i.getTipo() == 'CADENA' and boolmin:
                clave = i.getLexema()
                
                textoSalida.configure(state='normal')
                textoSalida.insert(END, analizador.Minimo(clave) + '\n')
                textoSalida.configure(state='disabled')

                clave = ''
                boolmin = False

            #Contar si
            elif i.getLexema().lower() == 'contarsi':
                boolcontarsi = True
            
            elif i.getTipo() == 'CADENA' and boolcontarsi:
                clave = i.getLexema()
            elif i.getTipo() == 'NUMERO' and boolcontarsi:
                numero = i.getLexema()

                textoSalida.configure(state='normal')
                textoSalida.insert(END, analizador.ContarSi(clave,numero) + '\n')
                textoSalida.configure(state='disabled')

                clave = ''
                numero = 0
                boolcontarsi = False

            #Reporte html
            elif i.getLexema().lower()=='exportarreporte':
                boolreporte = True
            
            elif i.getTipo() == 'CADENA' and boolreporte:
                nombre = i.getLexema()
                analizador.exportarReporte(nombre) 
                nombre = ''
                boolreporte = False
        
    else:
        textoSalida.configure(state='normal')
        textoSalida.insert(END, "ERROR DE SINTAXIS O LEXICO :(")
        textoSalida.configure(state='disabled')
        analizador.imprimirErroresSintacticos()

    analizador.limpiarDatos()

# - - - - -INTERFAZ GRAFICA- - - - - #
# Root
ventana = Tk()
ventana.title("BIZDATA - PROGRAM")
ventana.iconbitmap(r"C:\Users\eg574\OneDrive\Escritorio\LFP_S2_2023_Proyecto2_202200031/LFP-Proyecto2/icon/scanner.ico")
ventana.config(bg="blue4")
ventana.resizable(True, True)

# Obtenemos las dimensiones de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()
# Calculamos la posición de la ventana para centrarla
x = int(ancho_pantalla/2 - 600)
y = int(alto_pantalla/2 - 350)
# Centramos la ventana
ventana.geometry("1200x600+{}+{}".format(x, y))

#Ventana de edicion y lectura de texto
textoEntrada = ScrolledText(ventana, wrap=tk.WORD, height=28, width=70, bg="white", fg="black", font=("Tahoma", 12))
textoEntrada.place(x=35, y=120)

textoSalida = ScrolledText(ventana, wrap=tk.WORD, height=28, width=70, bg="white",state='disabled', fg="black", font=("Tahoma", 12))
textoSalida.place(x=700, y=120)

#Botones
btnAbrirArchivo = Button(ventana, height=2, width=11, text="Abrir archivo", command = abrirArchvo1, background="greenyellow", font=("Arial",12), fg="black")
btnAbrirArchivo.place(x=315, y=50)

btnAnalizar = Button(ventana, height=2, width=10, text="Procesar", command=Compilar, background="greenyellow", font=("Arial",12), fg="black")
btnAnalizar.place(x=420, y=50)

btnReporeteTokensValidos = Button(ventana, height=2, width=12, text="Tokens válidos",command=reporteTokens, background="greenyellow", font=("Arial",12), fg="black")
btnReporeteTokensValidos.place(x=515, y=50)

btnReporeteTokensInvalidos = Button(ventana, height=2, width=10, text="Errores",command=reporteErrores, background="greenyellow", font=("Arial",12), fg="black")
btnReporeteTokensInvalidos.place(x=630, y=50)

btnReporeteGrpahviz = Button(ventana, height=2, width=8, text="Graficar" , command=analizador.generarArbol, background="greenyellow", font=("Arial",12), fg="black")
btnReporeteGrpahviz.place(x=720, y=50)

#Labels
labelEditor = Label (ventana, text ="EDITOR DE TEXTO", font=("Trebuchet MS", 15), background="#044D9A", fg="white")
labelEditor.place(x=60, y=58)

labelTerminal = Label (ventana, text ="CONSOLA", font=("Trebuchet MS", 15), background="#044D9A", fg="white")
labelTerminal.place(x=980, y=58)

ventana.mainloop()
