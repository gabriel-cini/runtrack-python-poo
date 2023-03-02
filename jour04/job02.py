class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom}.")

class Eleve(Personne):
    def __init__(self, nom, age):
        super().__init__(nom, age)

    def allerEnCours(self):
        print("Je vais en cours.")

class Professeur(Personne):
    def __init__(self, nom, age):
        super().__init__(nom, age)

    def enseigner(self):
        print("Le cours commence.")

# Création de l'élève
eleve = Eleve("Enzo", 15)
eleve.bonjour()
eleve.allerEnCours() 
eleve.age = 15 

# Création du professeur
professeur = Professeur("Monsieur Dupont", 40)
professeur.bonjour() 
professeur.enseigner() 




        