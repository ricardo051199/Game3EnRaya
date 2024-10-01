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
    
    def podaAlphaBeta(self):

        def valor_max_alpha_beta(e, alpha, beta):
            if self.testTerminal(e):
                return self.get_utilidad(e, self.estado.jugador)
            v = float('-inf')
            for a in self.jugadas(e):
                v = max(v, valor_max_alpha_beta(self.getResultado(e, a), alpha, beta))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        def valor_min_alpha_beta(e, alpha, beta):
            if self.testTerminal(e):
                return self.get_utilidad(e, self.estado.jugador)
            v = float('inf')
            for a in self.jugadas(e):
                v = min(v, valor_min_alpha_beta(self.getResultado(e, a), alpha, beta))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v
    
        alpha = float('-inf')
        beta = float('inf')
        mejor_movida = None
        for a in self.jugadas(self.estado):
            v = valor_min_alpha_beta(self.getResultado(self.estado, a), alpha, beta)
            if mejor_movida is None or v > alpha:
                mejor_movida = a
                alpha = v

        return mejor_movida
    
    def podaalphaBetaFunEval(self):
        pass
