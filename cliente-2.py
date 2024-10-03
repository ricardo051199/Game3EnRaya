import socketio
from AgenteTresEnRaya import AgenteTresEnRaya

# Conexión al servidor
sio = socketio.Client()

n = 4
k = 3

luis = AgenteTresEnRaya(n, n, k)

@sio.event
def connect():
    print('Conectado al servidor')

@sio.event
def tablero_actual(data):
    print("Tablero actualizado:")
    for fila in data['tablero']:
        print(fila)
    print("Movidas disponibles:", data['movidas'])

def main():
    sio.connect('http://127.0.0.1:5000')

    while True:
        jugada = input("Ingresa tu movimiento (formato: fila,columna): ")
        fila, columna = map(int, jugada.split(','))
        # Enviar el movimiento al servidor
        sio.emit('hacer_movimiento', {'movimiento': (fila, columna)})

if __name__ == '__main__':
    main()