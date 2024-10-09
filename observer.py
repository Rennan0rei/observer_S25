class Observer:
    def update(self, message):
        raise NotImplementedError("Subclasses devem implementar o método update")