class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut_commande = "en cours"

    def ajouter_plat(self, nom_plat, prix_plat):
        self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": self.__statut_commande}

    def annuler_commande(self):
        self.__statut_commande = "annulée"
        for plat in self.__plats_commandes.values():
            plat["statut"] = self.__statut_commande

    def __calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values() if plat["statut"] == "en cours")
        return total

    def afficher_commande(self):
        total_a_payer = self.__calculer_total()
        print(f"Numéro de commande : {self.__numero_commande}")
        print("Plats commandés:")
        for plat, details in self.__plats_commandes.items():
            print(f"- {plat} : {details['prix']} € - Statut : {details['statut']}")
        print(f"Total à payer : {total_a_payer} €")

    def calculer_TVA(self, taux_TVA):
        total = self.__calculer_total()
        TVA = total * taux_TVA
        return TVA

commande1 = Commande("CMD001")
commande1.ajouter_plat("Pizza", 12.5)
commande1.ajouter_plat("Salade", 8.0)
commande1.afficher_commande()
commande1.annuler_commande()
commande1.afficher_commande()
TVA_commande1 = commande1.calculer_TVA(0.20)
print(f"TVA pour la commande 1 : {TVA_commande1} €")
