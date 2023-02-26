from Tree import Tree
from Nodo import Nodo
from unCrypt import unCrypt
class creadorDeArbol:
    def __init__(self) -> None:
        self.arbol = Tree()
        self.uncrypt = unCrypt()
    def lector(self):
        with open('text.txt','r') as file: 
            for line in file:
                lista = line.split(sep=",")
                code = int(self.uncrypt.traducir(line[1]))
                nodoEncontrado = self.arbol.levelOrderSearch(code)
                if nodoEncontrado is not None:
                    nodo = self.arbol.addNode(data=code,name= line[0],canciones = line[3])
                else:
                    nodoEncontrado.songs.append(line[3])
        return self.arbol
