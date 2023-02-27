class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    
    def SePresenter(self):
        print("Je m'appelle", self.nom, self.prenom)

# Création de plusieurs instances de la classe Personne
personne1 = Personne("Doe", "John")
personne1.SePresenter()
personne2 = Personne("Dupond", "Jean")
personne2.SePresenter()





