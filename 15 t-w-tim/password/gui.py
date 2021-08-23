from tkinter.constants import ANCHOR
from typing import Sized
import verificador as ver
import tkinter

def campo():
    entrada = tkinter.Entry(raiz, width = "40")
    entrada.grid(row = 0, column = 0, padx = 5, pady = 5)
    entrada.columnconfigure( 0, weight = 2)
    return entrada

def verificar():
    boton = tkinter.Button(raiz, text = "VERIFICAR", command = llamada)
    boton.grid(row = 0 , column = 6, padx = 5, pady =5)

def llamada():
    pas = entrada.get()
    respuesta = ver.comprobar(pas)
    mensaje(respuesta)

def espacio():
    esp = tkinter.Frame(raiz)
    esp.grid(row =2, column =0, padx = 5, pady = 5, columnspan = 3)
    return esp

def holders():
    f1 = tkinter.Label(info, text = " ")
    f2 = tkinter.Label(info, text = " ")
    f3 = tkinter.Label(info, text = " ")

    f1.grid( row = 0, column = 0, columnspan = 99)
    f2.grid( row = 1, column = 0, columnspan = 99)
    f3.grid( row = 2, column = 0, columnspan = 99)
    return f1, f2, f3


def mensaje(res):
    print(res)
    color = res[3]
    f1.config( text = res[0], fg = color)
    f2.config( text = res[1], fg = color)
    f3.config( text = res[2], fg = color)

    
    


    

raiz = tkinter.Tk()
raiz.resizable( 0, 0)
entrada = campo()
info = espacio()
f1, f2, f3 = holders()
verificar()
raiz.mainloop()