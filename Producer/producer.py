from observables.subject import Subject
from observables.observer import Observer

class Producer(Subject):
    def produce_message(self, message):
        print(f"Produzindo mensagem: {message}")
        self.notify_observers(message)

# Concreto Observer
class ConcreteObserver(Observer):
    def update(self, message):
        print(f"Observer recebeu a mensagem: {message}")

# Uso
if __name__ == "__main__":
    producer = Producer()
    observer = ConcreteObserver()
    
    # Registrando o observer
    producer.register_observer(observer)

    # Produzindo uma mensagem
    producer.produce_message("Olá, mundo!")
