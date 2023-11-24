#QUESTÃO 1 

class Subject:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, value1, value2):
        for observer in self._observers:
            observer.update(value1, value2)


class Observer:
    def update(self, value1, value2):
        pass


class DivObserver(Observer):
    def update(self, value1, value2):
        print("Resultado da divisão: ", value1 // value2)


class ModObserver(Observer):
    def update(self, value1, value2):
        print("Resultado do resto: ", value1 % value2)


class MulObserver(Observer):
    def update(self, value1, value2):
        print("Resultado da multiplicação: ", value1 * value2)


# QUESTÃO 2 

class NewsSource:
    def __init__(self):
        self._observers = []
        self._news = None

    def register(self, observer):
        self._observers.append(observer)

    def unregister(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._news)

    def add_news(self, news):
        self._news = news
        self.notify_observers()


class NewsChannel:
    def __init__(self, name):
        self._name = name

    def update(self, news):
        print(f"{self._name} está transmitindo: {news}")


reuters = NewsSource()
fox_news = NewsChannel("Fox News")
cnn = NewsChannel("CNN")

reuters.register(fox_news)
reuters.register(cnn)

reuters.add_news("Últimas notícias de última hora!")
