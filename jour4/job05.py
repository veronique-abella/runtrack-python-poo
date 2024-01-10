import math

class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius

    def aire(self):
        return math.pi * self.radius ** 2

mon_rectangle = Rectangle(largeur=5, hauteur=3)
mon_cercle = Cercle(radius=4)

print("Aire du rectangle :", mon_rectangle.aire())
print("Aire du cercle :", mon_cercle.aire())
