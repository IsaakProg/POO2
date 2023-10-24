from abc import ABC, abstractmethod
#QUESTÃO 1

# Interface MotorVehicle
class MotorVehicle(ABC):

    @abstractmethod
    def build(self):
        pass

# Classe Motorcycle que implementa a interface MotorVehicle
class Motorcycle(MotorVehicle):
    
    def build(self):
        return "Construindo uma motocicleta"

# Classe Car que implementa a interface MotorVehicle
class Car(MotorVehicle):
    
    def build(self):
        return "Construindo um carro"

# Classe abstrata MotorVehicleFactory com um método factory createMotorVehicle
class MotorVehicleFactory(ABC):

    @abstractmethod
    def createMotorVehicle(self):
        pass

# Classe MotorcycleFactory que implementa o método factory createMotorVehicle
class MotorcycleFactory(MotorVehicleFactory):

    def createMotorVehicle(self):
        return Motorcycle()

# Classe CarFactory que implementa o método factory createMotorVehicle
class CarFactory(MotorVehicleFactory):

    def createMotorVehicle(self):
        return Car()

# Função para testar o código
def main():
    motorcycleFactory = MotorcycleFactory()
    carFactory = CarFactory()

    myMotorcycle = motorcycleFactory.createMotorVehicle()
    myCar = carFactory.createMotorVehicle()

    print(myMotorcycle.build())  # Saída: Construindo uma motocicleta
    print(myCar.build())  # Saída: Construindo um carro

# Executar a função main para testar o código
if __name__ == "__main__":
    main()

#QUESTÃO 2

from abc import ABC, abstractmethod

# Definição das cores como um Enum para simplicidade
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Interface do Produto
class Product(ABC):
    
    def __init__(self, color):
        self.color = color
    
    def GetColor(self):
        return self.color
    
    @abstractmethod
    def ToString(self):
        pass

# Produtos concretos
class ModernArmchair(Product):
    
    def __init__(self, color, width, height, depth):
        super().__init__(color)
        self.width = width
        self.height = height
        self.depth = depth
    
    def ToString(self):
        return f"Poltrona moderna de cor {self.GetColor().name}, dimensões {self.width}x{self.height}x{self.depth}"

class ModernCoffeeTable(Product):
    
    def __init__(self, color, height, length):
        super().__init__(color)
        self.height = height
        self.length = length
    
    def ToString(self):
        return f"Mesa de café moderna de cor {self.GetColor().name}, dimensões {self.height}x{self.length}"

class ModernSofa(Product):
    
    def __init__(self, color, width, height, depth):
        super().__init__(color)
        self.width = width
        self.height = height
        self.depth = depth
    
    def ToString(self):
        return f"Sofá moderno de cor {self.GetColor().name}, dimensões {self.width}x{self.height}x{self.depth}"

# Fábrica de móveis
class FurnitureFactory(ABC):
    
    @abstractmethod
    def MakeArmchair(self):
        pass
    
    @abstractmethod
    def MakeCoffeeTable(self):
        pass
    
    @abstractmethod
    def MakeSofa(self):
        pass

# Fábrica de móveis retro
class RetroFurnitureFactory(FurnitureFactory):
    
    def MakeArmchair(self):
        return ModernArmchair(Color.RED, 80, 90, 100)
    
    def MakeCoffeeTable(self):
        return ModernCoffeeTable(Color.GREEN, 40, 60)
    
    def MakeSofa(self):
        return ModernSofa(Color.BLUE, 200, 90, 100)

# Função principal para testar o código
def main():
    factory = RetroFurnitureFactory()
    
    armchair = factory.MakeArmchair()
    coffee_table = factory.MakeCoffeeTable()
    sofa = factory.MakeSofa()
    
    print(armchair.ToString())
    print(coffee_table.ToString())
    print(sofa.ToString())

# Executar a função main para testar o código
if __name__ == "__main__":
    main()
