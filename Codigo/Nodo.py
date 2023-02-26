class Nodo:
    def __init__(self,data:int , name:str, canciones:list ,level:int =0 ) -> None:
        self.nombre = name
        self.data = data
        self.level = level
        self.songs =[]
        self.songs = self.songs.append(canciones)
        self.LeftSon = None
        self.RightSon = None