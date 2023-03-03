class unCrypt:
    def __init__(self) -> None:
        #Se escribe el diccionario en str
        self.ABC = "abcdefghijklmnopqrstuvwxyz,-" 
        #Se crea un atributo diccionario
        self.dictCryp = {}
        #Se llena el diccionario con el crearDiccionario
        self.crearDict()
    def crearDict(self):
        #En python los strings son iterables, por ello aprovecho para 
        #crear un for que recorra el string y tome la letra como key para el dict
        # y la posicione de este como el valor correspondiente a esa key. 
        for i in range(len(self.ABC)):
            self.dictCryp[self.ABC[i]]=str(i)
    #En este codigo recibo un str el cual se encarga de convertirlo ene el criterio final.
    def traducir(self, objetivo):
        #creo un string vacio
        codigo = ""
        #Me aseguro que el parametro sea un str
        objetivo = str(objetivo)
        #Recorro el str y cada caracter lo comparo con el abecedario y si encuentra el caracter significa que
        #es una letra, entonces lo convierte al numero correspondiente a su posicion.
        #Por lo contrario si no esta en el abecedario significa que es un numero, y este solo se agrega.
        #Luego se retorna la concatenacion.
        for i in objetivo:
            if i in self.dictCryp:
                codigo = codigo+self.dictCryp[i]
            else:
                codigo = codigo+i
        return codigo