class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA)

    def afficher(self):
        print("Nom : ", self.nom)
        print("Prix HT : ", self.prixHT,"€")
        print("TVA : ", self.TVA)
        print("Prix TTC : ", self.CalculerPrixTTC())

    def modifier_nom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifier_prixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenir_nom(self):
        return self.nom

    def obtenir_prixHT(self):
        return self.prixHT

    def obtenir_TVA(self):
        return self.TVA
# Création de deux produits
p1 = Produit("Chaise", 50, 0.2)
p2 = Produit("Table", 100, 0.2)

# Affichage des informations des produits
p1.afficher()
p2.afficher()

# Modification du nom et du prix de chaque produit
p1.modifier_nom("Fauteuil")
p1.modifier_prixHT(70)

p2.modifier_nom("Bureau")
p2.modifier_prixHT(120)

# Affichage des nouvelles informations des produits
p1.afficher()
p2.afficher()
