class Student:
    def __init__(self, nom, prenom, num_etudiant):
        self._nom = nom
        self._prenom = prenom
        self._num_etudiant = num_etudiant
        self._credits = 0
        self._level = self._studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self._credits += credits
            self._level = self._studentEval()
        else:
            print("Le nombre de crédits ajouté doit être supérieur à zéro.")

    def _studentEval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Très bien"
        elif self._credits >= 70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    def studentInfo(self):
        print(f"Informations de l'étudiant:")
        print(f"Nom: {self._nom}")
        print(f"Prénom: {self._prenom}")
        print(f"Identifiant: {self._num_etudiant}")
        print(f"Niveau: {self._level}")

john_doe = Student("John", "Doe", 145)

john_doe.add_credits(30)
john_doe.add_credits(40)
john_doe.add_credits(25)

print(f"Total de crédits de John Doe: {john_doe._credits}")

john_doe.studentInfo()
