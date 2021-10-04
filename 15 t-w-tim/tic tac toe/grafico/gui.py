import tkinter

def icons(canva, icon): #cargo los iconos
    x = canva.createimage("x.png")
    o = canva.createimagen("circulo.png")
    basio = canva.createimage("blanco.png")
    return [basio, x, o]


def cant (): # pvp o pve
    pass


def selcion_icon(icon): # player seleciona su icono
    pass

def tablero(can, cuadros): #dibuja el tablero del juego

def mensaje(raiz, st): # muestra mensaje de victoria o otra info
    pass

def todo(raiz, user1 , user2): # frame principal para tablero nombre y puntuacion
    pass


def inicio(icon):
    raiz = tkinter.Tk()
    can = canva(raiz)
    ico = icons(can)
    return raiz, ico

def canva(raiz):
    can = tkinter(raiz)
    return can

def fin(raiz):
    raiz.mainloop()
