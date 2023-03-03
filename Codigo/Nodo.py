class Nodo:
    def __init__(self,data:int , name:str, canciones:list ,level:int =0, posx = 0, posy = 0 ) -> None:
        self.coords = [posx, posy]
        self.nombre = name
        self.data = data
        self.level = level
        self.songs =[]
        self.songs = self.songs.append(canciones)
        self.LeftSon = None
        self.RightSon = None
    def dameCoords(self):
        return self.coords
    def __repr__(self) -> str:
        return self.nombre
    