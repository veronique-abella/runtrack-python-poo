class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrage = kilometrage
        self._en_marche = False
        self._reservoir = 50

    # Assesseurs (getters)
    def getMarque(self):
        return self._marque

    def getModele(self):
        return self._modele

    def getAnnee(self):
        return self._annee

    def getKilometrage(self):
        return self._kilometrage

    def getEnMarche(self):
        return self._en_marche

    def getReservoir(self):
        return self._reservoir

    # Mutateurs (setters)
    def setMarque(self, nouvelle_marque):
        self._marque = nouvelle_marque

    def setModele(self, nouveau_modele):
        self._modele = nouveau_modele

    def setAnnee(self, nouvelle_annee):
        self._annee = nouvelle_annee

    def setKilometrage(self, nouveau_kilometrage):
        self._kilometrage = nouveau_kilometrage

    def demarrer(self):
        if self._verifier_plein():
            self._en_marche = True
            print("La voiture démarre.")
        else:
            print("La voiture ne peut pas démarrer. Réservoir presque vide.")

    def arreter(self):
        self._en_marche = False
        print("La voiture s'arrête.")

    def _verifier_plein(self):
        return self._reservoir > 5


ma_voiture = Voiture("Toyota", "Corolla", 2020, 20000)

print(f"Marque: {ma_voiture.getMarque()}")
print(f"Modèle: {ma_voiture.getModele()}")
print(f"Année: {ma_voiture.getAnnee()}")
print(f"Kilométrage: {ma_voiture.getKilometrage()}")

ma_voiture.demarrer()

print(f"La voiture est en marche : {ma_voiture.getEnMarche()}")

ma_voiture.arreter()
