class Nodo:
    def __init__(self, data:int, level=0) -> None:
        self.data = data
        self.level = level
        self.LeftSon = None
        self.RightSon = None