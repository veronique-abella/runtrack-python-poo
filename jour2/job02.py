class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages

    def getTitre(self):
        return self._titre

    def getAuteur(self):
        return self._auteur

    def getNbPages(self):
        return self._nb_pages

    def setTitre(self, nouveau_titre):
        self._titre = nouveau_titre

    def setAuteur(self, nouvel_auteur):
        self._auteur = nouvel_auteur

    def setNbPages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self._nb_pages = nouveau_nb_pages
        else:
            print("Le nombre de pages doit être un entier positif.")

mon_livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 100)

print(f"Titre : {mon_livre.getTitre()}")
print(f"Auteur : {mon_livre.getAuteur()}")
print(f"Nombre de pages : {mon_livre.getNbPages()}")

mon_livre.setTitre("Harry Potter")
mon_livre.setAuteur("J.K. Rowling")
mon_livre.setNbPages(300)

print(f"Nouveau titre : {mon_livre.getTitre()}")
print(f"Nouvel auteur : {mon_livre.getAuteur()}")
print(f"Nouveau nombre de pages : {mon_livre.getNbPages()}")

mon_livre.setNbPages(-50)
