class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnées du point : ({self.x}, {self.y})")

    def afficherX(self):
        print(f"Coordonnée x : {self.x}")

    def afficherY(self):
        print(f"Coordonnée y : {self.y}")

    def changerX(self, new_x):
        self.x = new_x

    def changerY(self, new_y):
        self.y = new_y

point = Point(3, 5)

point.afficherLesPoints() 

point.afficherX() 

point.afficherY() 

point.changerX(7)
point.changerY(9)

point.afficherLesPoints() 
