from abc import ABC, abstractmethod

#QUESTÃO 1

# Classe abstrata Móvel
class Mobilia(ABC):
    @abstractmethod
    def funcao_mobilia(self):
        pass

    @abstractmethod
    def mostrar_estilo(self):
        pass

# Classes de produtos concretos
class ArmarioClássico(Mobilia):
    def funcao_mobilia(self):
        return "Função do armário clássico"

    def mostrar_estilo(self):
        return "Estilo clássico"

class CadeiraClássica(Mobilia):
    def funcao_mobilia(self):
        return "Função da cadeira clássica"

    def mostrar_estilo(self):
        return "Estilo clássico"

class MesaJantarClássica(Mobilia):
    def funcao_mobilia(self):
        return "Função da mesa de jantar clássica"

    def mostrar_estilo(self):
        return "Estilo clássico"

# E assim por diante para as classes de móveis contemporâneos e escandinavos...

# Classe abstrata Fábrica de Móveis
class FabricaMobilia(ABC):
    @abstractmethod
    def criar_armario(self):
        pass

    @abstractmethod
    def criar_cadeira(self):
        pass

    @abstractmethod
    def criar_mesa_jantar(self):
        pass

# Classes de fábricas concretas
class FabricaMobiliaClássica(FabricaMobilia):
    def criar_armario(self):
        return ArmarioClássico()

    def criar_cadeira(self):
        return CadeiraClássica()

    def criar_mesa_jantar(self):
        return MesaJantarClássica()

# E assim por diante para as fábricas de móveis contemporâneos e escandinavos...

#QUESTÃO 2

from abc import ABC, abstractmethod

# Interface VeiculoMotorizado
class VeiculoMotorizado(ABC):
    @abstractmethod
    def montar(self):
        pass

# Interface VeiculoEletrico
class VeiculoEletrico(ABC):
    @abstractmethod
    def carregar(self):
        pass

# Classes concretas
class MotoFuturista(VeiculoMotorizado):
    def montar(self):
        print("Montando Moto Futurista")

class MotoProximaGeracao(VeiculoMotorizado):
    def montar(self):
        print("Montando Moto da Próxima Geração")

class CarroEletricoFuturista(VeiculoEletrico):
    def carregar(self):
        print("Carregando Carro Elétrico Futurista")

class CarroEletricoProximaGeracao(VeiculoEletrico):
    def carregar(self):
        print("Carregando Carro Elétrico da Próxima Geração")

# Interface de Fábrica Abstrata
class Corporacao(ABC):
    @abstractmethod
    def criarVeiculoMotorizado(self):
        pass
    
    @abstractmethod
    def criarVeiculoEletrico(self):
        pass

# Fábricas Concretas
class CorporacaoFuturista(Corporacao):
    def criarVeiculoMotorizado(self):
        return MotoFuturista()
    
    def criarVeiculoEletrico(self):
        return CarroEletricoFuturista()

class CorporacaoProximaGeracao(Corporacao):
    def criarVeiculoMotorizado(self):
        return MotoProximaGeracao()
    
    def criarVeiculoEletrico(self):
        return CarroEletricoProximaGeracao()

# Código cliente
if __name__ == "__main__":
    fabrica = CorporacaoFuturista()
    moto = fabrica.criarVeiculoMotorizado()
    carro = fabrica.criarVeiculoEletrico()
    
    moto.montar()
    carro.carregar()

#QUESTÃO 3

from abc import ABC, abstractmethod

# Interface para Arma
class Arma(ABC):
    @abstractmethod
    def funcao_util(self):
        pass

# Classes concretas para Arma
class Espada(Arma):
    def funcao_util(self):
        return "O resultado da Espada"

class Machado(Arma):
    def funcao_util(self):
        return "O resultado do Machado"

class BolaDeFogo(Arma):
    def funcao_util(self):
        return "O resultado da Bola de Fogo"

# Interface para Armadura
class Armadura(ABC):
    @abstractmethod
    def funcao_util(self):
        pass
    
    @abstractmethod
    def funcao_util_com_arma(self, colaborador: Arma):
        pass

# Classes concretas para Armadura
class ArmaduraCorporal(Armadura):
    def funcao_util(self):
        return "O resultado da Armadura Corporal"
    
    def funcao_util_com_arma(self, colaborador: Arma):
        resultado = colaborador.funcao_util()
        return f"O resultado da Armadura Corporal colaborando com ({resultado})"

class ArmaduraOrc(Armadura):
    def funcao_util(self):
        return "O resultado da Armadura Orc"
    
    def funcao_util_com_arma(self, colaborador: Arma):
        resultado = colaborador.funcao_util()
        return f"O resultado da Armadura Orc colaborando com ({resultado})"

class Capa(Armadura):
    def funcao_util(self):
        return "O resultado da Capa"
    
    def funcao_util_com_arma(self, colaborador: Arma):
        resultado = colaborador.funcao_util()
        return f"O resultado da Capa colaborando com ({resultado})"

# Interface para AbstractFactory
class FabricaAbstrata(ABC):
    @abstractmethod
    def criar_arma(self):
        pass
    
    @abstractmethod
    def criar_armadura(self):
        pass

# Fábricas concretas
class FabricaGuerreiro(FabricaAbstrata):
    def criar_arma(self):
        return Espada()
    
    def criar_armadura(self):
        return ArmaduraCorporal()

class FabricaOrc(FabricaAbstrata):
    def criar_arma(self):
        return Machado()
    
    def criar_armadura(self):
        return ArmaduraOrc()

class FabricaMago(FabricaAbstrata):
    def criar_arma(self):
        return BolaDeFogo()
    
    def criar_armadura(self):
        return Capa()
