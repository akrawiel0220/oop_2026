# Klasa = Szablon, Przepis
class Czlowiek:
    # Istota
    gatunek = "Homo Sapiens"
    def __init__(self, imie):
        # Konstruktor
        # Akt Istnienia
        print(f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie

# Powstawanie obiektu
# Gotowanie z przepisu
adam = Czlowiek("Adam") # a = 4 # a = int(4)
ewa= Czlowiek("Ewa") # a = 4 # a = int(4)
print(adam.gatunek)
print(ewa.gatunek)
print(adam.imie)