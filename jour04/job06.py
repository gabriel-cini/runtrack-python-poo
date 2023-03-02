class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}, Année: {self.annee}, Prix: {self.prix}")

    def demarrer(self):
        print("Attention, je roule.")


class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")

    def demarrer(self):
        print("La voiture démarre.")


class Moto(Vehicule):
    def __init__(self, marque, annee, prix):
        super().__init__(marque, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roue}")

    def demarrer(self):
        print("La moto démarre.")


voiture = Voiture("Renault", 2022, 15000)
voiture.informationsVehicule()
voiture.demarrer()

moto = Moto("Yamaha", 2020, 8000)
moto.informationsVehicule()
moto.demarrer()
