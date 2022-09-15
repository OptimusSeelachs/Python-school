import tkinter as tk
import random

spieler = []

#-----Wuerfel-----
class Wuerfel(object):
    def __init__(self):
        self.augenzahl = random.randint(1, 6)

    def wuerfeln(self):
        self.augenzahl = random.randint(1, 6)

#-----Spieler-----
class Spieler(object):
    def __init__(self):
        self.wuerfelguess = tk.IntVar()
        self.wuerfelguess.set(6)
        self.kontostand = 1000
        self.einsatz = tk.IntVar()
        self.einsatz.set(10)
        self.name = tk.StringVar()

    def einzahlen(self, betrag):
        global kontoLabel
        self.kontostand += betrag
        kontoLabel.configure(text=self.kontostand)

    def auszahlen(self, betrag):
        self.kontostand -= betrag

    def kontostandpruefen(self):
        return self.kontostand > 0
    

    
    
        

#-----Spiel------
class Spiel(object):
    def __init__(self):
        self.wuerfel = []
        self.wuerfel.append(Wuerfel())
        self.wuerfel.append(Wuerfel())
        self.wuerfel.append(Wuerfel())
        

    def wuerfelsetzen(self, wert):
        self.spieler.setzen(wert)

    def werfen(self):
        global wuerfelLabel
        for wuerfel in self.wuerfel:
            wuerfel.wuerfeln()
        wuerfelLabel.configure(text=" " + str(spiel.wuerfel[0].augenzahl) + "  " + str(spiel.wuerfel[1].augenzahl) + "  " + str(spiel.wuerfel[2].augenzahl) + " ")

    def gewinn(self):
            if self.spieler.kontostandpruefen():
                self.spieler.auszahlen(self.spieler.einsatz.get())
                treffer = 0
                for wuerfel in self.wuerfel:
                    if self.spieler.wuerfelguess.get() == wuerfel.augenzahl:
                        treffer += 1
                self.spieler.einzahlen(self.spieler.einsatz.get() * treffer)
            else:
                global root
                root.destroy()
                exit()

    def runde(self):
        self.werfen()
        self.gewinn()

 
#------GUI--------
root = tk.Tk()
spiel = Spiel()

spieleranzahl = tk.IntVar()

tk.Entry(root, text= "Spieleranzahl", textvariable = spieleranzahl).grid(row=4, column=1)

for i in range(2):
    tk.Label(root, text="Spieler " + str(i+1), fg="green", font=("Courier", 20)).grid(row=10 + i, column=0)

tk.Button(root, text="Spieleranzahl", command = spieler.append(Spieler)).grid(row=3, column=3)

tk.Label(root, text="Chuck a Luck", fg="green", font=("Courier", 50)).grid(row=0, column=0,columnspan=3)
tk.Label(root, text="Konto", bg="lightgreen").grid(row=1, column=0)
tk.Label(root, text="Guess", bg="lightgreen").grid(row=1, column=1)
tk.Label(root, text="Wuerfel", bg="lightgreen").grid(row=1, column=2)

kontoLabel = tk.Label(root, text=str(spiel.spieler.kontostand),bg="red")
kontoLabel.grid(row=2, column=0)

tk.Label(root, text="Einsatz:", font=("Courier", 20), bg="lightgreen").grid(row=3,column=0)

einsatzEntry = tk.Entry(root, textvariable=spiel.spieler.einsatz, bg="lightblue")
einsatzEntry.grid(row=4, column=0)

guessEntry = tk.Entry(root, textvariable=spiel.spieler.wuerfelguess, bg="lightblue")
guessEntry.grid(row=2, column=1)

wuerfelLabel = tk.Label(root, text=" " + str(spiel.wuerfel[0].augenzahl) + "  " + str(spiel.wuerfel[1].augenzahl) + "  " + str(spiel.wuerfel[2].augenzahl) + " ",bg="lightblue")
wuerfelLabel.grid(row=2, column=2)


tk.Button(root, text="Spielen!", command=spiel.runde).grid(row=4, column=2)


root.mainloop()
