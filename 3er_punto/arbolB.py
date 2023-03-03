"""
Se desea mostrar en un árbol B las letras del alfabeto para demostrar como un árbol B es usado y al mismo tiempo notar la diferencia entre los árboles binarios vistos en clase.
---código class Node y class BTree fueron sacados de Chatgpt---
"""
#Se importa la clase Digraph del módulo graphviz
from graphviz import Digraph

def graph_btree(node, dot=None):
    if dot is None:# Si el objeto Digraph() es None
        dot = Digraph() # entonces se creará un objeto Digraph()
        dot.attr('node', shape='rectangle') # Se configura el atributo node con forma de los nodos como rectángulos
    dot.node(str(node.keys)) # Se agrega un nodo nuevo al grafo Digraph con la clave actual del nodo del árbol B, se mostrará como una cadena de caracteres
    for child in node.children: # Se itera sobre los hijos del nodo actual 
        if child: # Si el hijo es True
            dot.node(str(child.keys)) # Se agrega un nuevo nodo al Digraph con la clave del nodo hijo actual
            dot.edge(str(node.keys), str(child.keys)) #Se agrega una arista dirigida desde el nodo actual actual hasta el nodo hijo
            graph_btree(child, dot) # Usando recursividad se llama a la función graph_tree() para crear los nodos y aristas para el hijo actual
    return dot # Retorna el objeto Digraph con los nodos y aristas creados

class Node:
    def __init__(self, leaf=False):
        self.keys = [] # Lista de claves almacenadas en el nodo
        self.children = [] # Lista de nodos hijos del nodo
        self.leaf = leaf # Indica si el nodo es una hoja o no

    def __str__(self):
        return str(self.keys) # Devuelve una representación en cadena de las claves del nodo


class BTree:
    def __init__(self, t):
        self.root = Node(leaf=True)# Crea un nodo raíz vacío y lo asigna al atributo root
        self.t = t # Asigna el grado mínimo del árbol al atributo t

    def search(self, k, x=None):
        if isinstance(x, Node): # Si x es un objeto de la clase Node
            i = 0 # Inicializa el índice i a cero
            while i < len(x.keys) and k > x.keys[i]: # Mientras i sea menor que el número de claves en x y k sea mayor que la clave en la posición i
                i += 1 # Incrementa i en uno
            if i < len(x.keys) and k == x.keys[i]: # Si i es menor que el número de claves en x y k es igual a la clave en la posición i
                return True # Devuelve True (se encontró la clave k)
            elif x.leaf: # Si x es una hoja (no tiene hijos)
                return False # Devuelve False (no se encontró la clave k)
            else: # Si x no es una hoja (tiene hijos)
                return self.search(k, x.children[i]) # Llama recursivamente al método search con la clave k y el hijo de x en la posición i como argumentos
        else: # Si x no es un objeto de la clase Node
            return self.search(k, self.root) # Llama al método search con la clave k y el nodo raíz como argumentos

    def insert(self, k):
        r = self.root # Asigna el nodo raíz a la variable r
        if len(r.keys) == (2 * self.t) - 1: # Si r está lleno (tiene 2t-1 claves)
            s = Node() # Crea un nuevo nodo vacío y lo asigna a la variable s
            self.root = s # Asigna s como el nuevo nodo raíz del árbol
            s.children.insert(0, r) # Inserta r como el primer hijo de s
            self._split_child(s, 0) # Llama al método _split_child con s y 0 como argumentos para insertar la clave k en el subárbol apropiado de s
            self._insert_non_full(s, k) # Llama al método _insert_non_full con s y k como argumentos para insertar la clave k en el subárbol apropiado de s 
        else:
            self._insert_non_full(r, k) # Llama al método _insert_non_full con r y k como argumentos para insertar la clave k en el subárbol apropiado de r

    def _insert_non_full(self, x, k):
        i = len(x.keys) - 1 # Se obtiene el índice del último elemento de las claves del nodo x
        if x.leaf: # Si x es una hoja
            x.keys.append(0) # Se añade una clave k en la lista
            while i >= 0 and k < x.keys[i]: # Mientras i sea mayor o igual que 0 y k sea menor que la clave en la posición i
                x.keys[i + 1] = x.keys[i] 
                i -= 1
            x.keys[i + 1] = k # Se inserta la clave en la posición i + 1
        else: # Si x no es una hoja
            while i >= 0 and k < x.keys[i]: # Mientras i sea mayor o igual que 0 y k sea menor que la clave en la posición i
                i -= 1 # Decrese i en uno
            i += 1 # Aumenta i en uno
            if len(x.children[i].keys) == (2 * self.t) - 1: # Se encuentra el hijo apropiado y se verifica si esta lleno
                self._split_child(x, i) # Si el hijo está lleno, se divide en dos
                if k > x.keys[i]:
                    i += 1
            self._insert_non_full(x.children[i], k) # Se inserta k en el hijo apropiado

    def _split_child(self, x, i):
        t = self.t # Se obtiene el valor de t
        y = x.children[i]#se divide un nodo "y"
        z = Node(leaf=y.leaf) # se crea un nuevo z con la misma profundidad que "y"
        x.children.insert(i + 1, z) # Se inserta el nuevo z en la posición i + 1
        x.keys.insert(i, y.keys.pop(t - 1)) # Se inserta la mediana de "y"
        z.keys = y.keys[t - 1:]# nodo z tiene misma profundidad que "y" y sus valores son igual o mayores que la mediana
        y.keys = y.keys[:t - 1]# nodo "y" tiene misma profundidad que z y sus valores menores que la mediana
        if not y.leaf: # si "y" no es una hoja, los hijos se distribuyen entre:
            z.children = y.children[t:]# Los hijos que se encuentran desde la mediana en adelante se guardan en el nodo "z"
            y.children = y.children[:t]# Los hijos que se encuentran antes de la mediana se guardan en el nodo "y"
    
    def delete(self, k):
        self._delete(self.root, k)# se busca primero la llave y recursivamente la elimina del árbol B
    

    def __str__(self):
        return str(self.root) # retorna una representación en cadena de la raíz del árbol
    
    
my_btree = BTree(2) # se da un factor de ramificación de 2
my_btree.insert("a") # se insertan 26 letras del alfabeto
my_btree.insert("b")
my_btree.insert("c")
my_btree.insert("d")
my_btree.insert("e")
my_btree.insert("f")
my_btree.insert("g")
my_btree.insert("h")
my_btree.insert("i")
my_btree.insert("j")
my_btree.insert("k")
my_btree.insert("l")
my_btree.insert("m")
my_btree.insert("n")
my_btree.insert("o")
my_btree.insert("p")
my_btree.insert("q")
my_btree.insert("r")
my_btree.insert("s")
my_btree.insert("t")
my_btree.insert("u")
my_btree.insert("v")
my_btree.insert("w")
my_btree.insert("x")
my_btree.insert("y")
my_btree.insert("z")


dot = graph_btree(my_btree.root) # la función graph_btree() permitirá crear un grafo del árbol
dot.render('btree_graph') # renderiza y guarda el gráfica generado por graph_btree() como un archivo



