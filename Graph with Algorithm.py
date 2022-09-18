
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
    def __init__(self):
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

    def addKante(self, nameStartKnoten:int, nameZielKnoten:int):
        self.KantenMenge.append([nameStartKnoten , nameZielKnoten])

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
    for i in range(anzahlKnoten+1):
        if i == 0:
            continue
        else:
            g.addKnoten(i, "u")
    for knoten in g.KnotenMenge:
        for i in range(round((len(g.KnotenMenge)+1)/2)):
            if i+1 == anzahlKnoten:
                break
            x = random.choice([0,1])
            if x == 1:
                g.addKante(knoten.name, i+1)
            else:
                continue

    print(g.KantenMenge)
    print(g.KnotenMenge)
randomGraph(10)

def shortestPath(nameStartKnoten:int, nameEndKnoten:int):
        A = []
        N = [Knoten(nameStartKnoten, 0)]           
        U = g.getAlleKnoten()
        
        while len(N) > 0:
            
            x = N[0]
            nachbarn = g.getAlleNachbarn(x.name)

            for nachbar in nachbarn:
                y = g.getKnoten(nachbar)
                    
                if nachbar == nameEndKnoten:               
                    y.incGewicht(x.gewicht+1)
                    y.addVorgaenger(x.name)
                    A.append(g.getKnoten(nameEndKnoten))
                elif y.gewicht == 'u':
                    y.incGewicht(x.gewicht+1)
                    y.addVorgaenger(x.name)
                    N.append(y)
            A.append(x)
            N.pop(0)

        pfadExistiert = False        
        for knoten in A:
            if knoten.name == nameEndKnoten:
                pfadExistiert = True
                print("Der kürzeste Weg von",nameStartKnoten ,"zu", nameEndKnoten, "beträgt", knoten.gewicht)
        if pfadExistiert == False:
            print("Keine Verbindung von", nameStartKnoten, "zu", nameEndKnoten)
        else:
            path = [nameEndKnoten]
            pathEnd = nameEndKnoten
            for i in range(len(A)):
                for knoten in A:
                    if knoten.name == pathEnd and knoten.name != nameStartKnoten:
                        path.append(knoten.getVorgaenger()[0])
                        pathEnd = knoten.getVorgaenger()[0]
            print("Route:")
            for i in range(len(path)-1,-1,-1):
                if i>0:
                    print(str(path[i])+"->", end="")
                else:
                    print(path[i])

shortestPath(2,6)

