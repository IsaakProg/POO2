# Classe base para drinks
class Drink:
    def getDescription(self):
        return "Drink desconhecido"

    def cost(self):
        return 0.0

# Classe para Caipira
class Caipira(Drink):
    def getDescription(self):
        return "Caipira"

    def cost(self):
        return 20.0

# Classe para Caipirinha
class Caipirinha(Drink):
    def getDescription(self):
        return "Caipirinha"

    def cost(self):
        return 25.0

# Classe Decorator
class Decorator(Drink):
    def __init__(self, drink):
        self.drink = drink

# Classes para aditivos
class Saque(Decorator):
    def getDescription(self):
        return self.drink.getDescription() + ", saquê"

    def cost(self):
        return self.drink.cost() + 5.0

class Abacaxi(Decorator):
    def getDescription(self):
        return self.drink.getDescription() + ", abacaxi"

    def cost(self):
        return self.drink.cost() + 3.0

# ... (outras classes de aditivos)

# Criando uma caipira de saquê, abacaxi, kiwi e açúcar
drink1 = Saque(Abacaxi((Caipira())))
print(drink1.getDescription())
print(drink1.cost())

# Criando uma caipira de vodka, morango e adoçante
drink2 = (Caipira())
print(drink2.getDescription())
print(drink2.cost())

# Criando uma caipirinha
drink3 = Caipirinha()
print(drink3.getDescription())
print(drink3.cost())


