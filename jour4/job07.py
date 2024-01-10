import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()

    def creer_paquet(self):
        couleurs = ['Cœur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        
        for couleur in couleurs:
            for valeur in valeurs:
                self.paquet.append(Carte(valeur, couleur))

    def melanger_paquet(self):
        random.shuffle(self.paquet)

    def tirer_carte(self):
        return self.paquet.pop()

class Blackjack:
    def __init__(self):
        self.jeu = Jeu()
        self.jeu.melanger_paquet()
        self.main_joueur = []
        self.main_croupier = []

    def distribuer_cartes(self):
        self.main_joueur.append(self.jeu.tirer_carte())
        self.main_croupier.append(self.jeu.tirer_carte())
        self.main_joueur.append(self.jeu.tirer_carte())
        self.main_croupier.append(self.jeu.tirer_carte())

    def calculer_points(self, main):
        total = 0
        as_count = 0
        
        for carte in main:
            if carte.valeur.isdigit():
                total += int(carte.valeur)
            elif carte.valeur in ['Valet', 'Dame', 'Roi']:
                total += 10
            else:
                as_count += 1
                total += 11
        
        while total > 21 and as_count > 0:
            total -= 10
            as_count -= 1
        
        return total

    def jouer(self):
        self.distribuer_cartes()
        print("Main du joueur :")
        self.afficher_main(self.main_joueur)
        print("Main du croupier :")
        self.afficher_main(self.main_croupier[0:1])

        while True:
            choix = input("Voulez-vous prendre une carte ? (oui/non) : ")
            if choix.lower() == "oui":
                self.main_joueur.append(self.jeu.tirer_carte())
                print("Main du joueur :")
                self.afficher_main(self.main_joueur)
                if self.calculer_points(self.main_joueur) > 21:
                    print("Vous avez dépassé 21. Vous avez perdu.")
                    return "croupier_win"
            else:
                break

        print("Main complète du croupier :")
        self.afficher_main(self.main_croupier)

        while self.calculer_points(self.main_croupier) < 17:
            self.main_croupier.append(self.jeu.tirer_carte())
            print("Main du croupier :")
            self.afficher_main(self.main_croupier)

        points_joueur = self.calculer_points(self.main_joueur)
        points_croupier = self.calculer_points(self.main_croupier)

        print("Total joueur: ",points_joueur)
        print("Total croupier: ",points_croupier)

        if points_joueur > 21:
            print("Vous avez dépassé 21. Vous avez perdu.")
            return "croupier_win"
        elif points_croupier > 21:
            print("Le croupier a dépassé 21. Vous avez gagné.")
            return "joueur_win"
        elif points_joueur > points_croupier:
            print("Vous avez un total supérieur à celui du croupier. Vous avez gagné.")
            return "joueur_win"
        elif points_croupier > points_joueur:
            print("Le croupier a un total supérieur au vôtre. Vous avez perdu.")
            return "croupier_win"
        else:
            print("Égalité")
            return "egalite"

    def afficher_main(self, main):
        for carte in main:
            print(carte.valeur," de ",carte.couleur)


partie = Blackjack()
partie.jouer()
