import random
#import matplotlib as npl
#import matplotlib.pyplot as plt 
#import numpy as np


class Knoten(object):
    def __init__(self, name, xKoordinate, yKoordinate, besucht):
        self.name = name
        #self.laenge = ((nameStartKnoten.x - nameZielKnoten.x) ** 2 + (nameStartKnoten.y - nameZielKnoten.y) ** 2) ** (0.5)
        self.x = xKoordinate
        self.y = yKoordinate
        self.besucht = False
        self.vorgaenger = []

    def getX(self):
        return self.x

    def setX(self, neuesX:int):
        self.x = neuesX
        return self.x

    def getY(self):
        return self.y
    
    def setY(self, neuesY:int):
        self.y = neuesY
        return self.y

    def addVorgaenger(self, vorgaengerName:int):
        self.vorgaenger.append(vorgaengerName)
        
    def getVorgaenger(self):
        return self.vorgaenger
    
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

    def addKnoten(self, nameKnoten:int, xKoordinate:int, yKoordinate:int, besucht:bool):
        k = Knoten(nameKnoten, xKoordinate, yKoordinate, besucht)
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

    def addKante(self, nameStartKnoten:Knoten, nameZielKnoten:Knoten, besucht:Knoten):
        laenge = ((nameStartKnoten.x - nameZielKnoten.x) ** 2 + (nameStartKnoten.y - nameZielKnoten.y) ** 2) ** (0.5)
        self.KantenMenge.append([nameStartKnoten.name , nameZielKnoten.name, laenge, besucht.besucht])

    def delKante(self, nameStartKnoten:int, nameZielKnoten:int):
        for kante in self.KantenMenge:
            if kante[0] == nameStartKnoten and kante[1] == nameZielKnoten:
                self.KantenMenge.remove(kante)


    def getAlleNachbarn(self, nameKnoten:int):
        nachbarn = []
        for kante in self.KantenMenge:
            if kante[0] == nameKnoten:
                nachbarn.append(kante)
            elif kante[1] == nameKnoten:
                nachbarn.append(kante)
        return nachbarn

        print(nachbarn)
        print('Maul')
    
g = Graph()

def getVerbindung():
    for knoten in g.getAlleKnoten():
        print(knoten.name, ":", g.getAlleNachbarn(knoten.name))

def randomGraph(anzahlKnoten:int):

    for i in range(anzahlKnoten):
        xKoordinate = random.randint(0,100)
        yKoordinate = random.randint(0,100)
        besucht = False
        g.addKnoten(i, xKoordinate, yKoordinate, besucht)

    for knoten in g.KnotenMenge:
        for i in range(len(g.KnotenMenge)):
            if i+1 == anzahlKnoten:
                break
            elif knoten.name >= i+1:
                continue
            else:
                g.addKante(g.KnotenMenge[knoten.name], g.KnotenMenge[i+1], g.KnotenMenge[knoten.besucht])

    print(g.KantenMenge)
    print(g.KnotenMenge)
randomGraph(10)

def nearestNeighbour(g:Graph,startKnoten:int):
    A = []
    besuchteKnoten = [startKnoten]
    fremdeKnoten = g.getAlleKnoten
    naesterNachbar = 0
    kuerzesterWeg = 100

    while len(besuchteKnoten) != 0:
        print(len(besuchteKnoten))
        print(startKnoten)
        nachbarn = g.getAlleNachbarn(startKnoten)
       # del nachbarn('2')

        for nachbarKnoten in nachbarn:
            print(nachbarKnoten)
            print(nachbarKnoten[2])
            if kuerzesterWeg > nachbarKnoten[2] and nachbarKnoten[3] == False:
                kuerzesterWeg = nachbarKnoten[2]
                naesterNachbar = nachbarKnoten[0]
                print(kuerzesterWeg)
            nachbarKnoten[3] = True

        A.append(naesterNachbar)
        print(startKnoten)
        print(kuerzesterWeg)
        print(nachbarKnoten[3])
        print(A)
        #print(int(besuchteKnoten[startKnoten]))
       # fremdeKnoten = []
        besuchteKnoten.pop(0)
        #print(len(besuchteKnoten))

        startKnoten = naesterNachbar
    
nearestNeighbour(g,2)







#x = [1,2,3,4,5,6,7,8,9,10]
#y = [2,4,5,7,6,8,9,11,12,12]

#plt.scatter(x, y, label= 'Sterne', color= 'green', marker= '*', s=30)

#plt.xlabel('x - axis') 
#plt.ylabel('y - axis') 
#plt.title('My scatter plot!') 
#plt.legend()


#plt.show()
