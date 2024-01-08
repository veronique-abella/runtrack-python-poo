import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie

    def attaquer(self, cible):
        dommage = random.randint(5, 15)
        print(self.nom, "attaque ",cible.nom, "et lui inflige ",dommage, "points de dégâts.")
        cible.vie -= dommage

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        niveau = input("Choisissez le niveau de difficulté (facile, moyen, difficile) : ").lower()
        if niveau == "facile":
            self.niveau = 1
        elif niveau == "moyen":
            self.niveau = 2
        elif niveau == "difficile":
            self.niveau = 3
        else:
            print("Niveau non reconnu. Niveau par défaut : facile.")

    def lancerJeu(self):
        joueur = Personnage("Joueur", self.niveau * 50)
        ennemi = Personnage("Ennemi", self.niveau * 50)

        print("Vous affrontez un ennemi au niveau ",self.niveau," !")
        print(joueur.nom," a",joueur.vie," points de vie.")
        print(ennemi.nom," a",ennemi.vie," points de vie.")

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)
            if ennemi.vie <= 0:
                print(ennemi.nom," a été vaincu ! Félicitations, vous avez gagné !")
                break

            ennemi.attaquer(joueur)
            if joueur.vie <= 0:
                print(joueur.nom," a été vaincu. Vous avez perdu.")
                break

        print("Fin de la partie.")

jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
