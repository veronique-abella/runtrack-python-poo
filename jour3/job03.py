class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def __str__(self):
        return f"Titre : {self.titre}, Description : {self.description}, Statut : {self.statut}"

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                return True
        return False

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminée"
                return True
        return False

    def afficherListe(self):
        for tache in self.taches:
            print(tache)

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list

if __name__ == "__main__":
    tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
    tache2 = Tache("Réviser pour l'examen", "Relire les chapitres 5 et 6")
    tache3 = Tache("Faire du sport", "Aller à la salle de gym")

    liste_taches = ListeDeTaches()

    liste_taches.ajouterTache(tache1)
    liste_taches.ajouterTache(tache2)
    liste_taches.ajouterTache(tache3)

    print("Toutes les tâches :")
    liste_taches.afficherListe()

    liste_taches.supprimerTache("Faire du sport")

    print("\nTâches restantes :")
    liste_taches.afficherListe()

    liste_taches.marquerCommeFinie("Faire les courses")

    print("\nTâches restantes à faire :")
    taches_a_faire = liste_taches.filterListe("à faire")
    for tache in taches_a_faire:
        print(tache)
