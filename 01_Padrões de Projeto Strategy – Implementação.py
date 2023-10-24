from abc import ABC, abstractmethod

# Strategy Interface
class OrdenacaoStrategy(ABC):
    @abstractmethod
    def ordenar(self, lista):
        pass

# Concrete Strategies
class BubbleSort(OrdenacaoStrategy):
    def ordenar(self, lista):
        print("Ordenando com Bubble Sort")
        # Implementação do Bubble Sort

class InsertionSort(OrdenacaoStrategy):
    def ordenar(self, lista):
        print("Ordenando com Insertion Sort")
        # Implementação do Insertion Sort

class MergeSort(OrdenacaoStrategy):
    def ordenar(self, lista):
        print("Ordenando com Merge Sort")
        # Implementação do Merge Sort

class QuickSort(OrdenacaoStrategy):
    def ordenar(self, lista):
        print("Ordenando com Quick Sort")
        # Implementação do Quick Sort

# Context
class Personagem(ABC):
    def __init__(self, nickname, info):
        self.nickname = nickname
        self.info = info
        self.arma = None
        self.algoritmo = None  # Algoritmo de ordenação (Strategy)

    def saudacao(self):
        print(f"Olá, meu nome é {self.nickname}.")

    def lutar(self):
        if self.arma:
            self.arma.atacar()
        else:
            print("Estou lutando sem arma.")

    def atribuiArma(self, arma):
        self.arma = arma
        print(f"Estou usando {self.arma.nome}.")

    def atribuiAlgoritmo(self, algoritmo):
        self.algoritmo = algoritmo

    def executarOrdenacao(self, lista):
        if self.algoritmo:
            self.algoritmo.ordenar(lista)
        else:
            print("Algoritmo de ordenação não definido.")

# Classe abstrata para armas
class Arma(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def atacar(self):
        pass

# Classes concretas para armas
class Espada(Arma):
    def atacar(self):
        print(f"Atacando com {self.nome}, causando 10 de dano.")

class Machado(Arma):
    def atacar(self):
        print(f"Atacando com {self.nome}, causando 15 de dano.")

# Classes concretas para personagens
class Guerreiro(Personagem):
    def __init__(self, nickname):
        super().__init__(nickname, "Guerreiro")

# Código de execução
personagem = Guerreiro("Joaozinho")
personagem.saudacao()
personagem.lutar()

espada = Espada("Espada Mágica")
personagem.atribuiArma(espada)
personagem.lutar()

# Mudar estratégia de ordenação
bubble_sort = BubbleSort()
personagem.atribuiAlgoritmo(bubble_sort)
personagem.executarOrdenacao([3, 1, 4, 1, 5, 9])
