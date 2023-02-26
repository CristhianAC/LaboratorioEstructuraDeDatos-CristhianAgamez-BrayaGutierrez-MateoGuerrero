class creadorDeArbol:
    
    def lector(self):
        with open('text.txt','r') as file: 
            for line in file:
                lista = line.split(sep=",")