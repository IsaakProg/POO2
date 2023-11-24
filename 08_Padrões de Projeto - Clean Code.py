#Exercício 1: Nomes Significativos

def calcular_salario_liquido(salario_bruto):
    inss = 0.15 * salario_bruto
    irpf = 0.275 * salario_bruto
    return salario_bruto - inss - irpf

# Exemplo de uso:
salario_bruto = 10000
salario_liquido = calcular_salario_liquido(salario_bruto)
print(salario_liquido)

#Exercício 2: Comentários Desnecessários

def eh_par(numero):
    return numero % 2 == 0

#Exercício 3: Funções (Métodos)

def calcular_operacao_aritmetica(numero1, numero2, operacao):
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        return numero1 / numero2
    else:
        raise ValueError("Operação inválida")

#Exercício 4: Estruturas de Dados

alunos_notas = {
    "Ana": 8.5, "Bruno": 7.0, "Carla": 9.0, "Daniel": 6.5,
    "Eduardo": 10.0, "Fernanda": 8.0, "Gabriel": 7.5, "Helena": 9.5
}

media = sum(alunos_notas.values()) / len(alunos_notas)

for aluno, nota in alunos_notas.items():
    if nota > media:
        print(aluno, nota)

#Exercício 5: Espaçamento em Branco

def area_circulo(raio):
    return 3.14159 * raio ** 2

def volume_esfera(raio):
    return 4 / 3 * 3.14159 * raio ** 3

print(area_circulo(5))
print(volume_esfera(5))

#Exercício 6: Formatação de Linhas

def soma_quadrados(lista):
    return sum(x ** 2 for x in lista)

def media(lista):
    return sum(lista) / len(lista)

def variancia(lista):
    m = media(lista)
    return sum((x - m) ** 2 for x in lista) / len(lista)

def desvio_padrao(lista):
    return variancia(lista) ** 0.5

#Exercício 7: Funções com Muitos Parâmetros

class Pessoa:
    def __init__(self, nome, idade, cidade, pais, profissao, email):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.pais = pais
        self.profissao = profissao
        self.email = email

# Ou usar um dicionário para criar pessoa
def criar_pessoa(info_pessoa):
    # Código para criar uma pessoa usando info_pessoa que é um dicionário
    return Pessoa(**info_pessoa)
