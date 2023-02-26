from Tree import Tree
from unCrypt import unCrypt
class creadorDeArbol:
    def __init__(self) -> None:
        self.arbol = Tree()
        self.uncrypt = unCrypt()
    def lector(self):
        with open('text.txt','r') as file: 
            for line in file:
                lista = line.split(sep=",")
                nodo = self.arbol.addNode(data=int(self.uncrypt.traducir(line[1])),name= line[0],canciones = line[3])
        return self.arbol