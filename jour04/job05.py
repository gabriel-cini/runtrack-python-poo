class Forme:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    def aire(self):
        return self.longueur * self.largeur
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius
    
    def aire(self):
        return 3.14 * self.radius ** 2
# Création d'une instance de Rectangle
rectangle = Forme(10, 5)
# Calcul de l'aire du rectangle
aire_rectangle = rectangle.aire()
# Afficher  le résultat
print("Aire du rectangle : ", aire_rectangle)

# Création d'une instance de Cercle
cercle = Cercle(5)
# Calcul de l'aire du cercle
aire_cercle = cercle.aire()
# Affichage du résultat
print("Aire du cercle : ", aire_cercle)
