# Klasa = Szablon, Przepis
class Czlowiek:
    # Istota
    gatunek = "Homo Sapiens"
    def __init__ (self, imie):
        print (f"Niech powstanie czlowiek o imieniu {imie}")
        self.imie = imie

    def przedstaw_sie (self):
        print ("Dzien dobry, mam na imie {self.imie}")

    def przedstaw (self, osoba):
        print (f"Oto {osoba.imie}")
adam = Czlowiek ("Adam")
ewa = Czlowiek ("Ewa")g

ewa.przedstaw_sie()
ewa.przedstaw(adam)
