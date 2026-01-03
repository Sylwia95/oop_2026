# Klasa = Szablon, Przepis
class Czlowiek:
    # Istota
    gatunek = "Homo Sapiens"
    def __init__ (self, imie, plec):
        print (f"Niech powstanie czlowiek o imieniu {imie}")
        self.imie = imie
        self.plec = plec

    def przedstaw_sie (self):
        print ("Dzien dobry, mam na imie {self.imie} i jestem ", end ="")
        if self.plec == "M":
            print ("mezczyzna")
        else:
            print ("kobieta")

    def przedstaw (self, osoba):
        print (f"Oto {osoba.imie}")

class Dziecko(Czlowiek):

    def baw_sie(self):
        print ("Ale zabawa, juhuu!!!!")
    def przedstaw_sie (self):
        print (f"Cesc, jestem {self.imie} i jestem ", end ="")
        if self.plec == "M":
            print ("chlopcem")
        else:
            print ("dziewczynka")



adam = Czlowiek ("Adam", "M")
ewa = Czlowiek ("Ewa", "K")

ewa.przedstaw_sie()
ewa.przedstaw(adam)
kain = Dziecko("Kain", "M")
kain.baw_sie()
kain.przedstaw_sie()

