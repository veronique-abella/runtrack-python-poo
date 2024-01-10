class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, value):
        self.__longueur = value

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, value):
        self.__largeur = value

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, value):
        self.__hauteur = value

    def volume(self):
        return self.__hauteur * self.surface()


mon_rectangle = Rectangle(longueur=5, largeur=3)

print("Périmètre du rectangle :", mon_rectangle.perimetre())
print("Surface du rectangle :", mon_rectangle.surface())

mon_parallelepipede = Parallelepipede(longueur=5, largeur=3, hauteur=4)

print("Volume du parallélépipède :", mon_parallelepipede.volume())
