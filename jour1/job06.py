class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def afficherAge(self):
        print(f"L'âge de l'animal : {self.age} an")

    def vieillir(self):
        self.age += 1

    def nommer(self, nom):
        self.prenom = nom
        print(f"L'animal se nomme {self.prenom}")

mon_animal = Animal()

mon_animal.afficherAge()

mon_animal.vieillir()

mon_animal.afficherAge()

mon_animal.nommer("Luna")
