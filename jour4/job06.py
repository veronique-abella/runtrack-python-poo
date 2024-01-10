class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque = ",self.marque)
        print("Model = ",self.modele)
        print("Année = ",self.annee)
        print("Prix = ",self.prix)
    
    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de portes = ",self.portes)
    
    def demarrer(self):
        print("La voiture démarre.")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print("Nombre de roues = ",self.roues)
    
    def demarrer(self):
        print("La moto démarre.")


ma_voiture = Voiture(marque="Mercedes", modele="Classe A", annee=2020, prix=18500)
ma_moto = Moto(marque="Yamaha", modele="1200 Vmax", annee=1987, prix=4500)

ma_voiture.informationsVehicule()
ma_moto.informationsVehicule()
ma_voiture.demarrer()
ma_moto.demarrer()


