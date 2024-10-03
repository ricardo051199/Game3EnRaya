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
        self.acciones = self.podaAlphaBetaFunEval(self.estado)

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
        min_depth = 3
        base_depth = self.altura + self.k
        max_depth = max(min_depth, base_depth - len(self.jugadas(self.estado)) // max(1, (self.altura - self.k + 1)))

        def valor_max_alpha_beta(e, alpha, beta, depth=0):
            if self.testTerminal(e) or depth >= max_depth:
                return self.get_utilidad(e, self.estado.jugador)
            v = float('-inf')
            for a in self.jugadas(e):
                v = max(v, valor_min_alpha_beta(self.getResultado(e, a), alpha, beta, depth + 1))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        def valor_min_alpha_beta(e, alpha, beta, depth=0):
            if self.testTerminal(e) or depth >= max_depth:
                return self.get_utilidad(e, self.estado.jugador)
            v = float('inf')
            for a in self.jugadas(e):
                v = min(v, valor_max_alpha_beta(self.getResultado(e, a), alpha, beta, depth + 1))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v
        
        return max(self.jugadas(self.estado), key=lambda a: valor_min_alpha_beta(self.getResultado(self.estado, a), float('-inf'), float('inf'), 0))
    
    def podaAlphaBetaFunEval(self, estado):
        jugador = estado.jugador
        alpha = float('-inf')
        beta = float('inf')

        def valor_max_alpha_beta(e, alpha, beta, profundidad):
            if self.testTerminal(e):
                return self.get_utilidad(e, jugador)
            if profundidad == self.altura:
                return self.funcion_evaluacion(e)
            v = float('-inf')
            for a in self.jugadas(e):
                v = max(v, valor_min_alpha_beta(self.getResultado(e, a), alpha, beta, profundidad + 1))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        def valor_min_alpha_beta(e, alpha, beta, profundidad):
            if self.testTerminal(e):
                return self.get_utilidad(e, jugador)
            if profundidad == self.altura:
                return self.funcion_evaluacion(e)
            v = float('inf')
            for a in self.jugadas(e):
                v = min(v, valor_max_alpha_beta(self.getResultado(e, a), alpha, beta, profundidad + 1))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v

        mejor_movida = None
        for a in self.jugadas(estado):
            valor = valor_min_alpha_beta(self.getResultado(estado, a), alpha, beta, 0)
            if mejor_movida is None or valor > alpha:
                mejor_movida = a
                alpha = valor

        return mejor_movida
                                         
    def funcion_evaluacion(self, estado):
        puntaje = 0
        jugador = estado.jugador
        oponente = 'O' if jugador == 'X' else 'X'
        direcciones = [(1, 0), (0, 1), (1, 1), (1, -1)]
        for posicion in estado.tablero.keys():
            if estado.tablero[posicion] == jugador:
                for delta in direcciones:
                    longitud = self.contar_fichas(estado.tablero, posicion, jugador, delta)
                    puntaje += self.calcular_puntaje(longitud, jugador)
            elif estado.tablero[posicion] == oponente:
                for delta in direcciones:
                    longitud = self.contar_fichas(estado.tablero, posicion, oponente, delta)
                    puntaje -= self.calcular_puntaje(longitud, jugador)
        return puntaje

    def contar_fichas(self, tablero, posicion, jugador, delta_x_y):
        (delta_x, delta_y) = delta_x_y
        x, y = posicion
        longitud = 0

        centro_x = self.altura // 2
        centro_y = self.altura // 2
        
        while tablero.get((x, y)) == jugador:
            longitud += 1
            x, y = x + delta_x, y + delta_y

        x, y = posicion

        while tablero.get((x, y)) == jugador:
            longitud += 1
            x, y = x - delta_x, y - delta_y

        longitud -= 1

        return longitud

    def calcular_puntaje(self, longitud, jugador):
        if longitud >= self.k:
            return 100
        elif longitud == self.k - 1:
            return 50
        elif longitud == self.k - 2:
            return 5
        elif longitud == 1:
            return 1
        return 0



