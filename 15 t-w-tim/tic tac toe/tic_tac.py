from grafico import gui 


class Logic:

    end = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    def __init__(self):
         self.espacios() 
        
    def espacios(self):
        self.vals = ["blanco"] * 9

    def selec(self, pos, player):
        if self.vals[pos]:
            return 0
        self.vals[pos] = player.name()
        return 1

    def final(self):
        for i in end:
            if i[0] != "blanco" and i[0] == i[1] == i[2] :
                self.espacios()
                return 1
        return 0 

class Player:
    def __init__(self, imagen, nombre ):
        self.imagen = imagen
        self.victorias = 0
        self.nombre = nombre

    
if __name__ == "__main__":
    ico = []
    primer = 1
    raiz, ico  = gui.inicio()
    players = []
    if primer:
        
        gui.selcion_icon(players)

    gui.fin(raiz)