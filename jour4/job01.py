class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("L'âge de la personne est de ",self.age, "ans.")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai ",self.age,"ans.")


class Professeur:
    def __init__(self, matiereEnseignee):
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


une_personne = Personne()
un_eleve = Eleve()

print("L'âge par défaut de l'élève est :")
un_eleve.afficherAge()
