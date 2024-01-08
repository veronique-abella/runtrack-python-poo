class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts_marques = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts_marques += 1

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1

    def afficherStatistiques(self):
        print("Statistiques pour le joueur : ", self.nom)
        print("Numéro : ",self.numero,", Position : ",self.position)
        print(f"Buts marqués : ",self.buts_marques)
        print(f"Passes décisives effectuées : ",self.passes_decisives)
        print(f"Cartons jaunes reçus : ",self.cartons_jaunes)
        print(f"Cartons rouges reçus : ",self.cartons_rouges)
        print()


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste_joueurs = []

    def ajouterJoueur(self, joueur):
        self.liste_joueurs.append(joueur)

    def AfficherStatistiquesJoueurs(self):
        print("Statistiques des joueurs de l'équipe : ", self.nom)
        for joueur in self.liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.liste_joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()


joueur1 = Joueur("Lionel Messi", 10, "Attaquant")
joueur2 = Joueur("Cristiano Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Neymar Jr", 11, "Milieu")

equipe1 = Equipe("Barcelone")
equipe2 = Equipe("Real Madrid")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur2)

equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur("Lionel Messi", "but")
equipe1.mettreAJourStatistiquesJoueur("Neymar Jr", "passe")
equipe2.mettreAJourStatistiquesJoueur("Cristiano Ronaldo", "jaune")

equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()
