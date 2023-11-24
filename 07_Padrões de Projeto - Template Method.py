from abc import ABC, abstractmethod

# QUESTÃO 1
# Classe Abstrata
class StringTransformer(ABC):
    def template_method(self, text):
        transformed_text = self.transform(text)
        print(transformed_text)

    @abstractmethod
    def transform(self, text):
        pass

# Subclasse para Transformar em Maiúsculo
class UpperCaseTransformer(StringTransformer):
    def transform(self, text):
        return text.upper()

# Subclasse para Transformar em Minúsculo
class LowerCaseTransformer(StringTransformer):
    def transform(self, text):
        return text.lower()

# Subclasse para Inverter a String
class ReverseTransformer(StringTransformer):
    def transform(self, text):
        return text[::-1]

# Criação de Instâncias e Testes
def main():
    upper = UpperCaseTransformer()
    lower = LowerCaseTransformer()
    reverse = ReverseTransformer()

    # Testando as transformações
    text = "Olá Mundo"
    print("Original:", text)
    upper.template_method(text)
    lower.template_method(text)
    reverse.template_method(text)

if __name__ == "__main__":
    main()




# #QUESTÃO 2
from abc import ABC, abstractmethod

class PhoneOrderTemplate(ABC):
    def select_phone(self):
        pass

    def pack_phone(self):
        pass

    def make_payment(self):
        pass

    def deliver_phone(self):
        pass

    def process_order(self):
        self.select_phone()
        self.pack_phone()
        self.make_payment()
        self.deliver_phone()

class OnlineStore(PhoneOrderTemplate):
    def select_phone(self):
        print("Selecionando telefone no site da loja.")

    def pack_phone(self):
        print("Empacotando telefone no centro de distribuição.")

    def make_payment(self):
        print("Pagamento online realizado.")

    def deliver_phone(self):
        print("Telefone entregue pelo serviço de entrega.")

class OfflineStore(PhoneOrderTemplate):
    def select_phone(self):
        print("Selecionando telefone na loja física.")

    def pack_phone(self):
        print("Empacotando telefone na loja.")

    def make_payment(self):
        print("Pagamento realizado na loja.")

    def deliver_phone(self):
        print("Telefone entregue em mãos.")

# Testando o programa
if __name__ == "__main__":
    print("Processando pedido online:")
    online_store = OnlineStore()
    online_store.process_order()

    print("\nProcessando pedido offline:")
    offline_store = OfflineStore()
    offline_store.process_order()
