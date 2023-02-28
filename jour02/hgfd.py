class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def showName(self):
        return self.name
    # Privé
    def __setName(self):
        self.name = input('Quelle est votre nom ?')
    def getName(self):
        self.__setName()
        print(self.name)
    
gabriel = User('gabriel')
print(gabriel.getName) 