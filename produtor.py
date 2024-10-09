from observer import Subject

class Produtor(Subject):
    def __init__(self):
        super().__init__()
        # Armazena observadores organizados por tópicos
        self.topic_observers = {}

    # Registra um observador para um tópico específico
    def register_observer(self, observer, topic):
        if topic not in self.topic_observers:
            self.topic_observers[topic] = []
        self.topic_observers[topic].append(observer)

    # Envia uma mensagem apenas para os observadores registrados para o tópico específico
    def notify_observers(self, message, topic):
        if topic in self.topic_observers:
            for observer in self.topic_observers[topic]:
                observer.update(message)
        else:
            print(f"Nenhum observador registrado para o tópico '{topic}'.")

    # Método para produzir mensagens associadas a um tópico
    def produzir_mensagem(self, message, topic):
        print(f"Produzindo mensagem para o tópico '{topic}': {message}")
        self.notify_observers(message, topic)
    

