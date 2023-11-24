#QUESTÃO 1 
#CRIAR SERVIDOR SINGLETON

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.servers = []
        return cls._instance

    def add_server(self, server):
        if server.startswith('http://') or server.startswith('https://'):
            if server not in self.servers:
                self.servers.append(server)
                return True
        return False

    def get_http_servers(self):
        return [server for server in self.servers if server.startswith('http://')]

    def get_https_servers(self):
        return [server for server in self.servers if server.startswith('https://')]


# Testando o programa
if __name__ == "__main__":
    logger = Logger()
    print(logger.add_server('http://example.com'))  # Deve retornar True
    print(logger.add_server('https://example.com'))  # Deve retornar True
    print(logger.add_server('ftp://example.com'))  # Deve retornar False (não começa com http/https)
    print(logger.add_server('http://example.com'))  # Deve retornar False (duplicado)
    print(logger.get_http_servers())  # Deve retornar ['http://example.com']
    print(logger.get_https_servers())  # Deve retornar ['https://example.com']


#QUESTÃO 2
#IMPLEMENTAR SINGLETON 
#ZOOLOGICO VIRTUAL

class Zoo:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Zoo, cls).__new__(cls)
            cls._instance.animals = []
        return cls._instance

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)

    def get_animals(self):
        return self.animals


# Testando o programa
if __name__ == "__main__":
    zoo = Zoo()
    zoo.add_animal('Elefante')
    zoo.add_animal('Leão')
    zoo.add_animal('Zebra')
    print(zoo.get_animals())  # Deve retornar ['Elefante', 'Leão', 'Zebra']
