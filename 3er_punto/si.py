class Node:
    def __init__(self, leaf=False):
        self.keys = [] # Lista de claves almacenadas en el nodo
        self.children = [] # Lista de nodos hijos del nodo
        self.leaf = leaf # Indica si el nodo es una hoja o no

    def __str__(self):
        return str(self.keys) # Devuelve una representación en cadena de las claves del nodo


class BTree:
    def __init__(self, t):
        self.root = Node(leaf=True) # Crea un nodo raíz vacío y lo asigna al atributo root
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
            self._split_child(s, 0) # Llama al método _split_child con s y 0 como argumentos para dividir r en dos nodos y subir su clave mediana a s
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
            while i >= 0 and