class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)
    
    def surface(self):
        return self.__longueur * self.__largeur
    

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur
    
    def get_hauteur(self):
        return self.__hauteur
    
    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur
    
    def volume(self):
        return self.get_longueur() * self.get_largeur() * self.__hauteur
    # Crée un objet rectangle
r = Rectangle(4, 5)

# Afficher les résultats
print("Le périmètre du rectangle est :", r.perimetre()) 
print("La surface du rectangle est :", r.surface())    
r.set_longueur(6)
print("Le périmètre du rectangle est maintenant :", r.perimetre())  

p = Parallelepipede(4, 5, 6)
print("Le volume du parallélépipède est :", p.volume())    
p.set_longueur(6)
print("Le volume du parallélépipède est maintenant :", p.volume())     
