from AgenteTresEnRaya import AgenteTresEnRaya

class HumanoTresEnRaya(AgenteTresEnRaya):
    def __init__(self, h=3, v=3, k=3):
        AgenteTresEnRaya.__init__(self, h, v, k)

    def programa(self):
        print("Jugadas permitidas: {}".format(self.jugadas(self.estado)))
        print("")
        cad_movida = input('jugada? ')
        movida = eval(cad_movida)
        self.acciones = movida