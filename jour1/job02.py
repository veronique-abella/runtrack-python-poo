class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

op = Operation(nombre1=12, nombre2=3)

print(f"Le nombre1 est {op.nombre1}")
print(f"Le nombre2 est {op.nombre2}")
