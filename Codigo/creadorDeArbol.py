from Tree import Tree
from Nodo import Nodo

from unCrypt import unCrypt
class creadorDeArbol:
    def __init__(self) -> None:
        #Se instancia un arbol
        self.arbol = Tree()
        #Se intancia la manera de desencriptar los ids.
        self.uncrypt = unCrypt()
    def lector(self, nombreF):
        #Se abre el archivo en forma de lectura
        with open(nombreF,'r',encoding="utf-8") as file: 
            for line in file:
                lista = line.split(sep=",")
                #Se guarda el id en el code
                code = int(self.uncrypt.traducir(lista[1]))
                #Con el id busca el nodo a ver si se encuentra en el arbol, si no se encuentra en el lo agrega al arbol, de lo contrario
                #Solo agrega la cancion.
                nodoEncontrado = self.arbol.levelOrderSearch(code)
                if nodoEncontrado is None:
                    print(lista[3])
                    self.arbol.addNode(data=code,name=lista[0],canciones = str(lista[3]))
                elif nodoEncontrado is Nodo:
                    nodoEncontrado.songs.append(lista[3])
        #retorna el arbol
        return self.arbol
