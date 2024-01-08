class Ville:
    def __init__(self, nom, nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    def augmenter_population(self):
        self.__nombre_habitants += 1


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        self.__ville.augmenter_population()


ville_paris = Ville("Paris", 1000000)
ville_marseille = Ville("Marseille", 861635)

print(f"Population de la ville de {ville_paris._Ville__nom} : {ville_paris.get_nombre_habitants()}")
print(f"Population de la ville de {ville_marseille._Ville__nom} : {ville_marseille.get_nombre_habitants()}")

john = Personne("John", 45, ville_paris)
myrtille = Personne("Myrtille", 4, ville_paris)
chloe = Personne("Chloé", 18, ville_marseille)

john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()

print(f"Mise à jour de la population de la ville de {ville_paris._Ville__nom} {ville_paris.get_nombre_habitants()} habitants")
print(f"Mise à jour de la population de la ville de {ville_marseille._Ville__nom} {ville_marseille.get_nombre_habitants()} habitants")
