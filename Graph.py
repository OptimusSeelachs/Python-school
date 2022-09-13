class Graph(object):
    def __init__(self):
        self.Knoten = []
        self.Kanten = []

    def getAlleKnoten(self):
        return self.Knoten

    def existiertKnoten(self, nameKnoten:str):
        for knoten in self.Knoten:
            if knoten == nameKnoten:
                return True
            else:
                return False

    def addKnoten(self, nameKnoten:str):
        self.Knoten = self.Knoten + [nameKnoten]
        return self.Knoten

    def delKnoten(self, nameKnoten:str):
        for knoten in self.Knoten:
            if knoten == nameKnoten:
                self.Knoten.remove(nameKnoten)
            else:
                print("Kein Knoten mit diesem Namen")

    def existiertKante(self, nameStartKnoten:str, nameZielKnoten:str):
        for kante in self.Kanten:
            if kante[0] == nameStartKnoten and kante[1] == nameZielKnoten:
                return True
            else:
                return False

    def addKante(self, nameStartKnoten:str, nameZielKnoten:str):
        self.Kanten.append([nameStartKnoten , nameZielKnoten])

    def delKante(self, nameStartKnoten:str, nameZielKnoten:str):
        for kante in self.Kanten:
            if kante[0] == nameStartKnoten and kante[1] == nameZielKnoten:
                self.Kanten.remove(kante)


    def getAlleNachbarn(self, nameKnoten:str):
        nachbarn = []
        for kante in self.Kanten:
            if kante[0] == nameKnoten:
                nachbarn.append(kante[1])
        return nachbarn

g = Graph()
g.addKnoten("A")
g.addKnoten("B")
g.addKnoten("C")
g.addKante("A","B")
g.addKante("A","C")

def getVerbindung():
    for knoten in g.getAlleKnoten():
        print(knoten, ":", g.getAlleNachbarn(knoten))
getVerbindung()
