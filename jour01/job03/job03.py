class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    def addition(self):
        resultat = self.nombre1 + self.nombre2
        print("Le résultat de l'addition est :", resultat)
# Création d'une instance de la classe Operation
operation = Operation(12,3)
#Appel de la méthode addition pour effectuer l'addition et afficher le résultat
operation.addition()

