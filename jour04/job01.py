class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, new_age):
        self.age = new_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def affichageAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        super().__init__()
        self.matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")
# Instanciation d'un objet Personne avec l'âge
personne1 = Personne()

# Instanciation d'un objet Eleve
eleve1 = Eleve()

# Afficher l'âge par  de l'élève
eleve1.affichageAge() 

# Modificer l'âge de la personne
personne1.modifierAge(25)

# Appel de la méthode afficher l'âge de la personne
personne1.afficherAge() 

# Appel de la méthode bonjour de la personne
personne1.bonjour() 

# Appel de la méthode allerEnCours de l'élève
eleve1.allerEnCours()

# Appel de la méthode enseigner du professeur
professeur1 = Professeur("Mathématiques")
professeur1.enseigner() 
