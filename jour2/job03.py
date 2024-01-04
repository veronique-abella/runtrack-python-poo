class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages
        self._disponible = True

    def getTitre(self):
        return self._titre

    def getAuteur(self):
        return self._auteur

    def getNbPages(self):
        return self._nb_pages

    def verification(self):
        return self._disponible

    def emprunter(self):
        if self.verification():
            self._disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

    def rendre(self):
        if not self.verification():
            self._disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Le livre est déjà disponible.")

mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 100)

print("Le livre est disponible :", mon_livre.verification()) 

mon_livre.emprunter()

print("Le livre est disponible :", mon_livre.verification())

mon_livre.emprunter() 

mon_livre.rendre()

print("Le livre est disponible :", mon_livre.verification()) 

mon_livre.rendre()
