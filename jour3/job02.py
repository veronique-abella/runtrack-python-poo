class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print("Informations sur le compte : ")
        print("Numéro de compte : ", self.__numero_compte)
        print("Nom : ", self.__nom)
        print("Prénom : ", self.__prenom)
        print("Solde : ",self.__solde)
        print(f"Découvert autorisé : {'Oui' if self.__decouvert else 'Non'}")

    def afficherSolde(self):
        print("Le solde du compte est de : ", self.__solde)

    def versement(self, montant):
        self.__solde += montant
        print("Versement de ", montant, "€ effectué. Nouveau solde : ",self.__solde)

    def retrait(self, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            print("Retrait de ", montant, "€ effectué. Nouveau solde : ", self.__solde)
        else:
            print("Opération impossible : solde insuffisant.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            agios = self.__solde * taux_agios
            self.__solde -= agios
            print("Des agios de",agios,"€ ont été appliqués. Nouveau solde :",self.__solde)

    def virement(self, compte_destinataire, montant):
        if self.__solde >= montant or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print("Virement de ", montant, "€ effectué vers le compte", compte_destinataire, self.__numero_compte)
        else:
            print("Opération de virement impossible : solde insuffisant.")


compte1 = CompteBancaire("12345", "Doe", "John", 500, decouvert=False)
compte1.afficher()
compte1.afficherSolde()
compte1.versement(300)
compte1.retrait(200)
compte1.agios(0.05)
compte1.afficherSolde()

compte2 = CompteBancaire("54321", "Smith", "Alice", -100, decouvert=True)
compte2.afficher()
compte2.versement(200)

compte1.virement(compte2, 800)
compte1.afficher()
compte2.afficher()
