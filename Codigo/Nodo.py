class Nodo:
    def __init__(self,data:int , name:str, canciones:list ,level:int =0 ) -> None:
        self.nombre = name
        self.data = data
        self.level = level
        self.songs = canciones
        self.LeftSon = None
        self.RightSon = None