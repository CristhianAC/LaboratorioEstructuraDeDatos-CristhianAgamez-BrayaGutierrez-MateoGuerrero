from graphviz import Digraph

def graph_btree(node, dot=None):
    if dot is None:
        dot = Digraph()
        dot.attr('node', shape='rectangle')
    dot.node(str(node.keys))
    for child in node.children:
        if child:
            dot.node(str(child.keys))
            dot.edge(str(node.keys), str(child.keys))
            graph_btree(child, dot)
    return dot

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
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.children[i].keys) == (2 * self.t) - 1:
                self._split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self._insert_non_full(x.children[i], k)

    def _split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = Node(leaf=y.leaf)
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys.pop(t - 1))
        z.keys = y.keys[t - 1:]
        y.keys = y.keys[:t - 1]
        if not y.leaf:
            z.children = y.children[t:]
            y.children = y.children[:t]
    
    def delete(self, k):
        self._delete(self.root, k)
    

    def __str__(self):
        return str(self.root)
    
    



my_btree = BTree(2)
my_btree.insert("a")
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



dot = graph_btree(my_btree.root)
dot.render('btree_graph')



