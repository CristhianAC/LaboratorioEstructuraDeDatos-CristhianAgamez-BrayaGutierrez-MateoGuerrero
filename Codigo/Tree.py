from Nodo import Nodo
import networkx as nx
class Tree:
    
    def __init__(self, data = None) -> None:
        self.raiz = None
        if data is not None:
            self.raiz = Nodo(data)
    
    def addNode(self, data,name,canciones, currentNode=None):
        
        if self.raiz== None:
            nodo = Nodo(data, name= name, canciones= canciones)
            self.raiz = nodo
            print("Entré")
            return
        if currentNode == None:
            currentNode = self.raiz
        datoDeNodo=currentNode.data
        nodo = Nodo(data, level=currentNode.level+1, name= name, canciones= canciones)
        
        if data>datoDeNodo:
            if currentNode.RightSon == None:
                currentNode.RightSon = nodo 
            else:
                self.addNode(data = data, currentNode= currentNode.RightSon, name= name, canciones=canciones)
        elif data<datoDeNodo:
            if currentNode.LeftSon == None:
                currentNode.LeftSon = nodo 
            else:
                self.addNode(data, currentNode = currentNode.LeftSon, name = name, canciones= canciones)
    
    def levelOrderInsert(self, val, name, canciones):
        
        if self.raiz is None:
            self.raiz = Nodo(val)
            return 
        queue = []
        queue.append(self.raiz)
        
        while queue:
            node = queue.pop(0)
            if node.LeftSon is None:
                node.LeftSon = Nodo(val, level = node.level+1, name= name, canciones= canciones)
                return 
            else:
                queue.append(node.LeftSon)
            if node.RightSon is None:
                node.RightSon = Nodo(val, level = node.level+1, name= name, canciones= canciones)
                return 
            else:
                queue.append(node.RightSon)

    
    def llamarImpresiones(self, opciones):
        
        if (opciones == "inorden"):
            self.inordernRecursivo(self.raiz)
        elif(opciones == "preorden"):
            self.preordenRecursivo(self.raiz)
        elif(opciones== "postorden"):
            self.postordenRecursivo(self.raiz)

    
    def inordernRecursivo(self, node=None):
        
        if node is not None:
            self.inordernRecursivo(node.LeftSon)
            print(node.data, end="-> ")
            self.inordernRecursivo(node.RightSon)
    def agregadorDeVertices(self,node:Nodo, G:nx.Graph):
        if node is not None:
            if node.LeftSon is not None:
                G.add_edge(node.nombre, node.LeftSon.nombre)
                print("Agregué eje izq")
            if node.RightSon is not None:
                G.add_edge(node.nombre, node.RightSon.nombre)
                print("Agregué eje der")            
            self.agregadorDeVertices(node.LeftSon, G)
            self.agregadorDeVertices(node.RightSon, G) 
        
        
    def preordenRecursivo(self, node)-> None:
        
        
        if node is not None:
            print(node.data, end="-> ")            
            self.preordenRecursivo(node.LeftSon)
            self.preordenRecursivo(node.RightSon)  

    def postordenRecursivo(self, node)-> None:
        
        if node is not None:
            self.postordenRecursivo(node.LeftSon)
            self.postordenRecursivo(node.RightSon)
            print(node.data, end="-> ")
    
    
    def levelOrderSearch(self, value: int) -> Nodo:
        
        traversed = []
        traversed.append(self.raiz)
        if self.raiz is None:
            return None
        while traversed != []:
            if traversed[0].data == value:
                return traversed[0]
            x = traversed.pop(0) 
            if x.LeftSon != None:
                traversed.append(x.LeftSon)
            if x.RightSon != None:
                traversed.append(x.RightSon)
        return None
    def recorrer(self, nodos):
        traversed = []
        
        traversed.append(self.raiz)
        if self.raiz is None:
            return None
        while traversed != []:
            
            x = traversed.pop(0)
            nodos.append(x)
            if x.LeftSon != None:
                traversed.append(x.LeftSon)
            if x.RightSon != None:
                traversed.append(x.RightSon)
        return nodos
    
    def buscaElMenor(self, nodo=None) -> int:
        
        if nodo == None:
            nodo = self.raiz
        if nodo.LeftSon is None:
            return nodo
        else: 
            return self.buscaElMenor(nodo.LeftSon)
    def buscaElMayor(self, nodo=None) -> int:
        
        if nodo == None:
            nodo = self.raiz
        if nodo.RightSon is None:
            return nodo
        else: 
            return self.buscaElMayor(nodo.RightSon)
    def buscarLvl(self, data):
        
        traversed = []
        traversed.append(self.raiz)
        if self.raiz is None:
            return None
        while traversed != []:
            if traversed[0].data == data:
                levelDelNodo = traversed[0].level
                return levelDelNodo
            x = traversed.pop(0) 
            if x.LeftSon != None:
                traversed.append(x.LeftSon)
            if x.RightSon != None:
                traversed.append(x.RightSon)
        
        return None
    
    
    def buscarCamino(self, nodoActual, nodoObjetivo, camino):
        

        if nodoActual is None:
            return None
        
        camino.append(nodoActual)  
        
        if nodoActual.data == nodoObjetivo:
            return camino
        
        camino_izq = self.buscarCamino(nodoActual.LeftSon, nodoObjetivo, camino)  
        camino_der = self.buscarCamino(nodoActual.RightSon, nodoObjetivo, camino)  
        
        if camino_izq is None and camino_der is None:
            camino.pop()  
        
        return camino_izq or camino_der