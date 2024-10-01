from AgenteTresEnRaya import AgenteTresEnRaya
from Tablero import Tablero
from HumanoTresEnRaya import HumanoTresEnRaya

luis = AgenteTresEnRaya()
juan = HumanoTresEnRaya()

tablero = Tablero()

tablero.insertar_objeto(luis)
tablero.insertar_objeto(juan)
tablero.run()
