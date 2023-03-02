class Forme:
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

# créer un objet Rectangle
rectangle = Rectangle(5, 10)

# imprimer l'aire du rectangle
print("L'aire du rectangle est de ",rectangle.aire())  
