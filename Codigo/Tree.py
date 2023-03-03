from Nodo import Nodo
import networkx as nx
class Tree:
    
    def __init__(self, data = None) -> None:
        self.raiz = None
        if data is not None:
            self.raiz = Nodo(data)

    def get_height(self, node: Nodo):
        if node is None:
            return 0
        return node.height

    def get_balance(self, node: Nodo):
        if node is None:
            return 0
        return self.get_height(node.LeftSon) - self.get_height(node.RightSon)
    
    def rotate_right(self, node: Nodo):
        left_node = node.LeftSon
        right_of_left = left_node.RightSon

        left_node.RightSon = node
        node.LeftSon = right_of_left

        node.height = max(self.get_height(node.LeftSon), self.get_height(node.RightSon)) + 1
        left_node.height = max(self.get_height(left_node.LeftSon), self.get_height(left_node.RightSon)) + 1

        return 

    def rotate_left(self, node: Nodo):
        right_node = node.RightSon
        left_of_right = right_node.LeftSon

        right_node.left = node
        node.RightSon = left_of_right

        node.height = max(self.get_height(node.LeftSon), self.get_height(node.RightSon)) + 1
        right_node.height = max(self.get_height(right_node.LeftSon), self.get_height(right_node.RightSon)) + 1

        return right_node
    
    def addNode(self, data,name,canciones, currentNode: Nodo =None):
        
        if self.raiz== None:
            nodo = Nodo(data, name= name, canciones= canciones)
            self.raiz = nodo
            return

        if currentNode == None:
            currentNode = self.raiz
        datoDeNodo=currentNode.data
        
        

        if data>datoDeNodo:
            if currentNode.RightSon == None:
                coords = currentNode.dameCoords()
                nivel =currentNode.level+1
                nodo = Nodo(data, level=nivel, name= name, canciones= canciones, posx =coords[0]+(1.333333)/nivel, posy=coords[1]-1.33333)
                currentNode.RightSon = nodo 

                nodo.height = max(self.get_height(nodo.LeftSon), self.get_height(nodo.RightSon)) + 1
                balance = self.get_balance(nodo)
                
                if balance > 1 and data < nodo.LeftSon.data:
                    return self.rotate_right(nodo)
                
                if balance < -1 and data > nodo.RightSon.data:
                    return self.rotate_left(nodo)

                if balance > 1 and data > nodo.LeftSon.data:
                    nodo.LeftSon = self.rotate_left(nodo.LeftSon)
                    return self.rotate_right(nodo) 
                
                if balance < -1 and data < nodo.RightSon.data:
                    nodo.RightSon = self.rotate_right(nodo.RightSon)
                    return self.rotate_left(nodo)
                

            else:
                self.addNode(data = data, currentNode= currentNode.RightSon, name= name, canciones = canciones)
        elif data<datoDeNodo:
            
            if currentNode.LeftSon == None:
                coords = currentNode.dameCoords()
                nivel =currentNode.level+1
                nodo = Nodo(data, level=nivel, name= name, canciones= canciones, posx = coords[0]-(1.33333)/nivel, posy = coords[1]-1.33333)
                currentNode.LeftSon = nodo

                nodo.height = max(self.get_height(nodo.LeftSon), self.get_height(nodo.RightSon)) + 1
                balance = self.get_balance(nodo)
                
                if balance > 1 and data < nodo.LeftSon.data:
                    return self.rotate_right(nodo)
                
                if balance < -1 and data > nodo.RightSon.data:
                    return self.rotate_left(nodo)

                if balance > 1 and data > nodo.LeftSon.data:
                    nodo.LeftSon = self.rotate_left(nodo.LeftSon)
                    return self.rotate_right(nodo) 
                
                if balance < -1 and data < nodo.RightSon.data:
                    nodo.RightSon = self.rotate_right(nodo.RightSon)
                    return self.rotate_left(nodo)


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
                G.add_edge(node.data, node.LeftSon.data)
            if node.RightSon is not None:
                G.add_edge(node.data, node.RightSon.data)
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
        x = traversed.pop(0)
        nodos.append(x)
        if x is not None:
            traversed.append(x.LeftSon)
            traversed.append(x.RightSon)
        
        while traversed != []:
            
            
            size = len(nodos)
            espar = size%2==0
            
            if espar:
                index_p = (size-2)/2
            else:
                index_p = (size-1)/2
            if (nodos[int(index_p)] == None):
                nodos.append(None)
            else:
                x = traversed.pop(0)
                nodos.append(x)
                if x is not None:
                    traversed.append(x.LeftSon)
                    traversed.append(x.RightSon)
            
        
        return nodos
    
    def delete_node(self, node: Nodo, data):
        if node is None:
            return node

        elif data < node.data:
            node.LeftSon = self.delete_node(node.LeftSon, data)

        elif data > node.data:
            node.RightSon = self.delete_node(node.RightSon, data)    

        else:
            # El nodo no tiene hijos
            if node.LeftSon is None:
                temp = node.RightSon
                node = None
                return 

            elif node.RightSon is None:
                temp = node.LeftSon
                node = None
                return

            # El nodo tiene 2 hijos, se busca el inorder succesor
            temp = self.buscaElMenor(node.RightSon)

            # Se copia el valor del inorder succesor al nodo 
            node.data = temp.data

            # Se elimina el inorder succesor (debido a que ya se guardo en otro lugar, en la linea aterior) 
            node.RightSon = self.delete_node(node.RightSon, temp.data)

        # Por si el arbol solo tiene un nodo 
        if node is None:
            return 
        
        # Se actualiza la altura del nodo acutual 
        node.height = 1 + max(self.get_height(node.LeftSon),self.get_height(node.RightSon))

        # Se obtiene el balance del nodo
        balance = self.get_balance(node)

        # Caso izquierda-izquierda 
        if balance > 1 and self.get_balance(node.LeftSon) >= 0:
            return self.rotate_right(node)

        # Caso izquierda-derecha
        if balance > 1 and self.get_balance(node.LeftSon) < 0:
            node.LeftSon = self.rotate_left(node.LeftSon)  
            return self.rotate_right(node)
        
        # Caso derecha-derecha 
        if balance < -1 and self.get_balance(node.RightSon) <= 0:
            return self.rotate_left(node)
        
        # Caso derecha-izquierda
        if balance < -1 and self.get_balance(node.RightSon) > 0:
            node.RightSon = self.rotate_right(node.RightSon)
            return self.rotate_left(node)
        
        return node

    def buscaElMenor(self, nodo=None) -> Nodo:
        
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