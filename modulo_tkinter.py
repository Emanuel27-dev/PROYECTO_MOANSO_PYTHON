from tkinter import *

# https://living-sun.com/es/python/716977-how-do-i-get-rid-of-python-tkinter-root-window-python-winapi-tkinter-tk.html
# link para ocultar, mostrar y eliminar una ventana.

def crear_ventana(dimension,titulo=None,back_ground=None):

    ventana = Toplevel()
    ventana.geometry(dimension)
    ventana.title(titulo)
    ventana.resizable(False,False)
    ventana.config(bg=back_ground,cursor="hand1")

    return  ventana


def crear_boton(ventana,texto,funcion=None):

    boton = Button(ventana,text=texto,command=funcion)
    boton.config(bd=4,font=("Terminal 9 bold"))

    return  boton


def crear_etiqueta(ventana,texto):

    # ejemplo de fuente => font=("Helvetica 12 bold")
    # cargar una imagen => Label(image= variable_imagen)
    etiqueta = Label(ventana,text=texto)
    etiqueta.config(bg="#0B7D8F",font=("Helvetica 12 bold"))

    return etiqueta


def crear_entrada(ventana,variable=None):

    entrada = Entry(ventana,textvariable=variable)
    entrada.config(bd=5,font=("Terminal 12 bold"))
    return entrada


