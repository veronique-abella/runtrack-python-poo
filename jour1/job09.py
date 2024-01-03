class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def calculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        infos = f"Nom du produit : {self.nom}\n"
        infos += f"Prix HT : {self.prixHT}\n"
        infos += f"TVA : {self.TVA}%\n"
        infos += f"Prix TTC : {self.calculerPrixTTC()}"
        return infos

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prix):
        self.prixHT = nouveau_prix

    def retournerNom(self):
        return self.nom

    def retournerPrixHT(self):
        return self.prixHT


produit1 = Produit("Ordinateur", 800, 20)
produit2 = Produit("Téléphone", 500, 15)

print(produit1.afficher())
print("\n")
print(produit2.afficher())
print("\n")

produit1.modifierNom("Nouvel ordinateur")
produit1.modifierPrixHT(900)
produit2.modifierNom("Nouveau téléphone")
produit2.modifierPrixHT(600)

print(f"Nouveau prix du {produit1.retournerNom()} : {produit1.retournerPrixHT()}")
print(f"Nouveau prix du {produit2.retournerNom()} : {produit2.retournerPrixHT()}")
