class unCrypt:
    def __init__(self) -> None:
        self.ABC = "abcdefghijklmnopqrstuvwxyz" 
        self.dictCryp = {}
        self.crearDict()
    def crearDict(self):
        for i in range(len(self.ABC)):
            self.dictCryp[self.ABC[i]]=str(i)
    def traducir(self, objetivo):
        codigo = ""
        objetivo = str(objetivo)
        for i in objetivo:
            if i in self.dictCryp:
                codigo = codigo+self.dictCryp[i]
            else:
                codigo = codigo+i
        return codigo