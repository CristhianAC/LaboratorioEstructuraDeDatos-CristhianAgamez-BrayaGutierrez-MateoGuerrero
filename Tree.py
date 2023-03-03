from Nodo import Nodo
class Tree:
    
    def __init__(self, data) -> None:
        self.raiz = Nodo(data)
    
    def addNode(self, data, currentNode=None):
        if currentNode == None:
            currentNode = self.raiz
        datoDeNodo=currentNode.data
        nodo = Nodo(data, level=currentNode.level+1)
        
        if data>datoDeNodo:
            if currentNode.RightSon == None:
                currentNode.RightSon = nodo 
            else:
                self.addNode(data, currentNode.RightSon)
        elif data<datoDeNodo:
            if currentNode.LeftSon == None:
                currentNode.LeftSon = nodo 
            else:
                self.addNode(data, currentNode.LeftSon) 
    
    def levelOrderInsert(self, val):
        
        if self.raiz is None:
            self.raiz = Nodo(val)
            return 
        queue = []
        queue.append(self.raiz)
        
        while queue:
            node = queue.pop(0)
            if node.LeftSon is None:
                node.LeftSon = Nodo(val, level = node.level+1)
                return 
            else:
                queue.append(node.LeftSon)
            if node.RightSon is None:
                node.RightSon = Nodo(val, level = node.level+1)
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
    
    
    def levelOrderSearch(self, value: int):
        
        traversed = []
        traversed.append(self.raiz)
        if self.raiz is None:
            return None
        while traversed != []:
            if traversed[0].data == value:
                return traversed[0]
            x = traversed.pop(0) 
            if x.LeftSon != None:
                traversed.extend(x.LeftSon)
            if x.RightSon != None:
                traversed.extend(x.RightSon)
        return None
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
    
    

    def punto1(self, nodo1, nodo2):
        
        camino1 = self.buscarCamino(self.raiz, nodo1, [])  
        camino2 = self.buscarCamino(self.raiz, nodo2, []) 
        
        i = 0
        while i < len(camino1) and i < len(camino2) and camino1[i] == camino2[i]:
            i += 1
            
        
        return camino1[i-1]  
    
    
    
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