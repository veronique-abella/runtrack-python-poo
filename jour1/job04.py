class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        return f"Je suis {self.nom} {self.prenom}"

personne1 = Personne("John", "Doe")
personne2 = Personne("Jean", "Dupont")

print(personne1.SePresenter())
print(personne2.SePresenter())

