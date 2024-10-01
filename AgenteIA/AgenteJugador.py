#################################################################
# Nombre      : Entorno                                         #
# Version     : 0.05.03.2017                                    #
# Autor       : Victor                                          #
# Descripcion : Clase Agentes con Adversarios                   #
##################################################################


from AgenteIA.Agente import Agente
from collections import namedtuple


ElEstado = namedtuple('ElEstado', 'jugador, get_utilidad, tablero, movidas')


class AgenteJugador(Agente):

    def __init__(self):
        Agente.__init__(self)
        self.estado = None
        self.juego = None
        self.utilidad = None

    def jugadas(self, estado):
        raise Exception("Error: No se implemento")

    def get_utilidad(self, estado, jugador):
        raise Exception("Error: No se implemento")

    def testTerminal(self, estado):
        return not self.jugadas(estado)

    def getResultado(self, estado, m):
        raise Exception("Error: No se implemento")

    def programa(self):

        # self.acciones = self.minimax()
        self.acciones = self.podaAlphaBeta()
        # self.acciones = self.podaalphaBetaFunEval(self.estado, self.estado.jugador)

    def minimax(self):

        def valorMax(e):
            if self.testTerminal(e):
                return self.get_utilidad(e, self.estado.jugador)
            v = -100
            for a in self.jugadas(e):
                v = max(v, valorMin(self.getResultado(e, a)))
            return v

        def valorMin(e):
            if self.testTerminal(e):
                return self.get_utilidad(e, self.estado.jugador)
            v = 100
            for a in self.jugadas(e):
                v = min(v, valorMax(self.getResultado(e, a)))
            return v

        return max(self.jugadas(self.estado), key=lambda a: valorMin(self.getResultado(self.estado, a)))
