import random

class Knoten(object):
    def __init__(self, name, gewicht):
        self.name = name
        self.gewicht = gewicht 
        self.vorgaenger = []

    def addVorgaenger(self, vorgaengerName:int):
        self.vorgaenger.append(vorgaengerName)
        
    def getVorgaenger(self):
        return self.vorgaenger

    def incGewicht(self, inc:int):
        if self.gewicht == "u":
            self.gewicht = inc
    
    def setName(self, randomName:int):
        self.name = randomName
        return self.name

    def getName(self):
        return self.name
            
class Graph(object):
    def __init__(self, ):
        self.KnotenMenge = []
        self.KantenMenge = []

    def getAlleKnoten(self):
        return self.KnotenMenge

    def existiertKnoten(self, nameKnoten:int):
        for knoten in self.KnotenMenge:
            if knoten == nameKnoten:
                return True
            else:
                return False

    def addKnoten(self, nameKnoten:int, gewichtKnoten:int):
        k = Knoten(nameKnoten,gewichtKnoten)
        self.KnotenMenge.append(k)
       

    def getKnoten(self, nameKnoten:int):
        for knoten in self.KnotenMenge:
            if knoten.name == nameKnoten:
                return knoten

    def delKnoten(self, nameKnoten:int):
        for knoten in self.KnotenMenge:
            if knoten.name == nameKnoten:
                self.KnotenMenge.remove(nameKnoten)
            else:
                print("Kein Knoten mit diesem Namen")
    

    def existiertKante(self, nameStartKnoten:int, nameZielKnoten:int):
        for kante in self.KantenMenge:
            if kante[0] == nameStartKnoten and kante[1] == nameZielKnoten:
                return True
            else:
                return False

    def addKante(self, nameStartKnoten:int, nameZielKnoten:int, laenge:int):
        self.KantenMenge.append([nameStartKnoten , nameZielKnoten, laenge])



    def delKante(self, nameStartKnoten:int, nameZielKnoten:int):
        for kante in self.KantenMenge:
            if kante[0] == nameStartKnoten and kante[1] == nameZielKnoten:
                self.KantenMenge.remove(kante)


    def getAlleNachbarn(self, nameKnoten:int):
        nachbarn = []
        for kante in self.KantenMenge:
            if kante[0] == nameKnoten:
                nachbarn.append(kante[1])
        return nachbarn

    
g = Graph()

def getVerbindung():
    for knoten in g.getAlleKnoten():
        print(knoten.name, ":", g.getAlleNachbarn(knoten.name))

def randomGraph(anzahlKnoten:int):
    for i in range(anzahlKnoten):
        g.addKnoten(i, "u")
    for knoten in g.KnotenMenge:
        for i in range(len(g.KnotenMenge)):
            if i+1 == anzahlKnoten:
                break
            elif knoten.name == i+1:
                continue
            else:
                y = random.randint(0,11)
                g.addKante(knoten.name, i+1, y)

    print(g.KantenMenge)
    print(g.KnotenMenge)
randomGraph(10)
