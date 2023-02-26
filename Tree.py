from Nodo import Nodo
class Tree:
    #Inicializo arbol con raiz incluida
    def __init__(self, data) -> None:
        self.raiz = Nodo(data)
    #Agrego nodos en caso de que sea un arbol binario de busqueda, haciendo comparacion si el dato a 
    #agregar es mayor o menor, a la vez el nodo tiene un atributo nivel y cuando encuentro un espacio para el nodo
    #simplemente le sumo uno al nivel del nodo anterior y se lo agrego al nodo actual.
    def addNode(self, data, currentNode=None):
        if currentNode == None:
            currentNode = self.raiz
        datoDeNodo=currentNode.data
        nodo = Nodo(data, level=currentNode.level+1)
        #Se compara si el dato del nodo a crearse es mayor o menor que el dato del nodo actual.
        #Una vez realiza la comparacion evalua si el lado al cual se le asignara estipulado por las reglas
        #de los arboles binarios de busqueda el cual si es menor se le asignará como hijo izquierdo y si es mayor se 
        #asignará al lado derecho una vez decida donde lo guardará revisa si el espacio esta vacio y si no lo esta se le aplicará
        #otra vez esta misma funcion al hijo que se encontró.
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
    #Esta funcion se encarga de rellenar un arbol por nivel.
    def levelOrderInsert(self, val):
        
        if self.raiz is None:
            self.raiz = Nodo(val)
            return 
        queue = []
        queue.append(self.raiz)
        #Se crea una cola donde se llenará por nivel de izquierda derecha y checkeará los hijos de los miembros de la cola
        #y eliminará posteriormente, si encuentra un nodo el cual le falta un hijo simplemente creará un nuevo
        #nodo y se lo asignará en el espacio para así intentar que sea un arbol lo mas completo posible. 
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

    #Funcion que se encarga de llamar cada una de las posibles maneras de recorrer un arbol (Inorden, preorder y postorden)
    def llamarImpresiones(self, opciones):
        
        if (opciones == "inorden"):
            self.inordernRecursivo(self.raiz)
        elif(opciones == "preorden"):
            self.preordenRecursivo(self.raiz)
        elif(opciones== "postorden"):
            self.postordenRecursivo(self.raiz)

    #Estructuras de recorrer un arbol inorden, preorden, postorden
    def inordernRecursivo(self, node=None):
        
        #Si el nodo no esta vacio, imprimirá el hijo izquierdo, luego imprimirá el nodo 
        # y luego el hijo derecho y se repite hasta el extremo de la rama de manera recursiva
        if node is not None:
            self.inordernRecursivo(node.LeftSon)
            print(node.data, end="-> ")
            self.inordernRecursivo(node.RightSon)


    def preordenRecursivo(self, node)-> None:
        
        #Si el nodo no está vacio imprime el dato del nodo, luego llama esta misma funcion al izquierdo y luego
        # al derecho de manera recursiva
        if node is not None:
            print(node.data, end="-> ")            
            self.preordenRecursivo(node.LeftSon)
            self.preordenRecursivo(node.RightSon)  

    def postordenRecursivo(self, node)-> None:
        #Si el nodo no está vacio llamará de manera recursiva al hijo izquiero y luego al hijo derecho, 
        # posteriormente imprimira el nodo.
        if node is not None:
            self.postordenRecursivo(node.LeftSon)
            self.postordenRecursivo(node.RightSon)
            print(node.data, end="-> ")
    ####################################################################
    #Algoritmo de busqueda en arbol por nivel 
    def levelOrderSearch(self, value: int):
        #Se crea una lista o cola donde se guardará de izquierda a derecha por nivel cada uno de los hijos de los nodos
        #Situados, posteriormente cada elementeo se compara con el dato que se busca y si ese no es se agregaran sus hijos a la lista.
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
        #Al ser un arbol binario de busqueda simplemente se moverá al hijo izquierdo mas bajo del arbol. y este
        # se consigue bajando al hijo izquierdo de cada nodo de manera recursiva hasta que el hijo izquierdo del nodo en el que te ubiques sea none.
        # Eso significará que en el nodo que te encuentras es el nodo menor.
        if nodo == None:
            nodo = self.raiz
        if nodo.LeftSon is None:
            return nodo
        else: 
            return self.buscaElMenor(nodo.LeftSon)
    def buscaElMayor(self, nodo=None) -> int:
        #Al ser un arbol binario de busqueda simplemente se moverá al hijo derecho mas bajo del arbol. y este
        # se consigue bajando al hijo derecho de cada nodo de manera recursiva hasta que el hijo derecho del nodo en el que te ubiques sea none.
        # Eso significará que en el nodo que te encuentras es el nodo mayor.
        if nodo == None:
            nodo = self.raiz
        if nodo.RightSon is None:
            return nodo
        else: 
            return self.buscaElMayor(nodo.RightSon)
    def buscarLvl(self, data):
        #Este es el mismo algoritmo de busqueda por nivel que previamente expliqué con la diferencia de que este no retorna el nodo.
        #Sinó el nivel del nodo
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
    
    #Esta funcion se encarga de implementar la funcion buscarCamino

    def punto1(self, nodo1, nodo2):
        #guardo en camino 1 y camino 2 , una lista con todos los nodos que hay que recorrer para llegar
        # a los 2 objetivos
        camino1 = self.buscarCamino(self.raiz, nodo1, [])  
        camino2 = self.buscarCamino(self.raiz, nodo2, []) 
        #Se crea un contador que inicie desde 0 para recorrer los caminos hasta que uno de los dos se acabe o hasta que el camino
        #Deje de ser igual, justo en el punto que el camino es distinto o que simplemente el camino se acaba, se encuentra
        #El ancestro común mas lejano de la raíz
        i = 0
        while i < len(camino1) and i < len(camino2) and camino1[i] == camino2[i]:
            i += 1
            
        #Aquí simplemente retorno el anterior al ultimo que se guarda porque al entrar la ultima vez se sumará una vez
        #mas de las necesarias, siendo el penultimo el ancestro comun mas lejano.
        return camino1[i-1]  
    
    
    
    def buscarCamino(self, nodoActual, nodoObjetivo, camino):
        #Este condicional ayuda a que si se ingresa un nodo que es none simplemente indique no 
        # retorne nada, ya que este no seria el camino.

        if nodoActual is None:
            return None
        #Si pasó el condicional significa que este si podria ser un camino, entonces se agregaria el nodo en el que se encuentra 
        # a la lista del camino.
        camino.append(nodoActual)  
        #Si se encuentra el nodo en el camino simplemente retornar el camino creado
        if nodoActual.data == nodoObjetivo:
            return camino
        #Aqui simplemente recorro toda las posibilidades de los hijos de cada nodo ya sea por la izquierda o la derecha,
        #hasta encontrar el hijo.
        camino_izq = self.buscarCamino(nodoActual.LeftSon, nodoObjetivo, camino)  
        camino_der = self.buscarCamino(nodoActual.RightSon, nodoObjetivo, camino)  
        #Lo anterior se dá si simplemente es el camino correcto, este condicional ayuda a borrar el dato 
        # si este no es el camino correcto, simplemente se borra.
        if camino_izq is None and camino_der is None:
            camino.pop()  
        # aquí solamente se retorna el camino correcto.
        return camino_izq or camino_der