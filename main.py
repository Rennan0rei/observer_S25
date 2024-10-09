from Producer.producer import Producer
from Consumer.consumer import Consumer

def main():
    # Criando instâncias do Producer e do Consumer
    producer = Producer()
    consumer1 = Consumer()
    consumer2 = Consumer()

    # Registrando os consumidores
    producer.register_observer(consumer1)
    producer.register_observer(consumer2)

    # Produzindo algumas mensagens
    producer.produce_message("Olá, mundo do consumidor!")
    producer.produce_message("Mensagem adicional para os consumidores.")

if __name__ == "_main_":
    main()