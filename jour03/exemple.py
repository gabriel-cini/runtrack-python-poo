class CompteA:
    def __init__(self,solde):
        self.solde = solde
    def virement(self,montant,compte):
        if self.solde > montant:
            self.solde -= montant
            compte.solde += montant
        else:
            print("Pas assez d'argent")

class CompteB:
    def __init__(self,solde):
        self.solde = solde

comptea = CompteA(1000)
compteb = CompteB(500)
print(comptea.solde)
print(compteb.solde)
        
        