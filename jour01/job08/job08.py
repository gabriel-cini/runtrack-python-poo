import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    
    def changerRayon(self, rayon):
        self.rayon = rayon
    
    def afficherInfos(self):
        
        print("Rayon :", self.rayon)
        print("Diamètre :", self.diametre())
        print("Circonférence :", self.circonference())
        print("Aire :", self.aire())

    
    def circonference(self):
        return 2 * math.pi * self.rayon
    
    def aire(self):
        return math.pi * self.rayon ** 2
    
    def diametre(self):
        return 2 * self.rayon

#Instanciation des cercles
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# affichage des informations des cercles
print("Cercle 1 :")
cercle1.afficherInfos()

print("\nCercle 2 :")
cercle2.afficherInfos()
