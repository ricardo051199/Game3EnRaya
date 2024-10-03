from AgenteTresEnRaya import AgenteTresEnRaya
from Tablero import Tablero
from HumanoTresEnRaya import HumanoTresEnRaya

if __name__ == "__main__": 
    n = 4
    k = 3
    luis = AgenteTresEnRaya(n, n, k)
    juan = HumanoTresEnRaya(n, n, k)
    juan.tecnica = "podaalfabeta"
    # juan.tecnica = "minmax"
    tablero = Tablero(n, n)    
    tablero.insertar_objeto(luis)
    tablero.insertar_objeto(juan)
    tablero.run()