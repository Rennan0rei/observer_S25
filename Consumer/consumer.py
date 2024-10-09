from observables.observer import Observer
from Producer.producer import Producer
class Consumer(Observer):
    def update(self, message):
        # Simulando processamento da mensagem
        print(f"Consumer processando a mensagem: {message}")
        self.consume_message(message)
    
    def consume_message(self, message):
        # Processamento específico da mensagem
        print(f"Mensagem consumida: {message}")

# Uso
if __name__ == "__main__":
    producer = Producer()
    consumer = Consumer()
    
    # Registrando o consumidor (observer)
    producer.register_observer(consumer)

    # Produzindo uma mensagem
    producer.produce_message("Mensagem para o consumidor")
