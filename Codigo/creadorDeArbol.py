from Tree import Tree
from Nodo import Nodo

from unCrypt import unCrypt
class creadorDeArbol:
    def __init__(self) -> None:
        self.arbol = Tree()
        self.uncrypt = unCrypt()
    def lector(self, nombreF):
        with open(nombreF,'r',encoding="utf-8") as file: 
            for line in file:
                lista = line.split(sep=",")
                code = int(self.uncrypt.traducir(lista[1]))
                nodoEncontrado = self.arbol.levelOrderSearch(code)
                if nodoEncontrado is None:
                    
                    nodo = self.arbol.addNode(data=code,name=lista[0],canciones = lista[3])
                elif nodoEncontrado is Nodo:
                    nodoEncontrado.songs.append(lista[3])
        return self.arbol
