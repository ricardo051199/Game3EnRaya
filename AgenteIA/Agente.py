class Agente:

    def __init__(self, programa=None):
        self.vive = True
        self.percepciones = []
        self.acciones = None

    def esta_vivo(self):
        return self.vive

    def programa(self):
        raise Exception("Debe implementarse el programa agente")
