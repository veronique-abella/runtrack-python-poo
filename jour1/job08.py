import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"Rayon du cercle : {self.rayon}")
        print(f"Diamètre du cercle : {self.diametre()}")
        print(f"Circonférence du cercle : {self.circonférence()}")
        print(f"Aire du cercle : {self.aire()}")

    def circonférence(self):
        return 2 * math.pi * self.rayon

    def aire(self):
        return math.pi * (self.rayon ** 2)

    def diametre(self):
        return 2 * self.rayon


cercle1 = Cercle(4)
cercle2 = Cercle(7)

print("Informations pour le premier cercle :")
cercle1.afficherInfos()

print("\nInformations pour le deuxième cercle :")
cercle2.afficherInfos()
