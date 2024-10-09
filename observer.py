class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses devem implementar o método update")


class Subject:
    def __init__(self):
        self.observers = []


    def register_observer(self, observer):
        self.observers.append(observer)


    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)