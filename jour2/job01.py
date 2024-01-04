class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    def getLongueur(self):
        return self._longueur

    def getLargeur(self):
        return self._largeur

    def setLongueur(self, nouvelle_longueur):
        self._longueur = nouvelle_longueur

    def setLargeur(self, nouvelle_largeur):
        self._largeur = nouvelle_largeur


mon_rectangle = Rectangle(10, 5)

print(f"Longueur initiale : {mon_rectangle.getLongueur()}")
print(f"Largeur initiale : {mon_rectangle.getLargeur()}")

mon_rectangle.setLongueur(15)
mon_rectangle.setLargeur(7)

print(f"Nouvelle longueur : {mon_rectangle.getLongueur()}")
print(f"Nouvelle largeur : {mon_rectangle.getLargeur()}")
