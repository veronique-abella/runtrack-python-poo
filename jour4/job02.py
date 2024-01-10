class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("L'âge de la personne est de ", self.age,"ans.")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, new_age):
        self.age = new_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai ",self.age, "ans.")


class Professeur:
    def __init__(self, matiereEnseignee, age):
        self.matiereEnseignee = matiereEnseignee
        self.age = age
    
    def bonjour(self):
        print("Hello")

    def enseigner(self):
        print("Le cours va commencer")


un_eleve = Eleve()

print("Bonjour de l'élève :")
un_eleve.bonjour()
print("L'élève dit :")
un_eleve.allerEnCours()

un_eleve.modifierAge(15)
print("L'âge de l'élève a été redéfini :")
un_eleve.afficherAge()

un_professeur = Professeur(matiereEnseignee="Mathématiques", age=40)

print("Bonjour du professeur :")
un_professeur.bonjour()
print("Le professeur commence le cours :")
un_professeur.enseigner()
