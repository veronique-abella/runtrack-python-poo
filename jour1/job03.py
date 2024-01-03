class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print(f"La somme de nombre1 et nombre2 est : {resultat}")

op = Operation(nombre1=12, nombre2=3)

op.addition()
