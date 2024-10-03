from flask import Flask
from flask_socketio import SocketIO, emit
from Tablero import Tablero

app = Flask(__name__)
socketio = SocketIO(app)

n = 4
k = 3
tablero = Tablero(n, n)

@app.route('/')
def index():
    return "Servidor de Tres en Raya en ejecución."

@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')
    emit('estado_juego', {'tablero': tablero.juegoActual.tablero, 'movidas': tablero.juegoActual.movidas})

@socketio.on('jugada')
def handle_jugada(data):
    jugador = data['jugador']
    movida = tuple(data['movida'])
    print(f"Recibiendo jugada de {jugador}: {movida}")

    # Realizar la jugada en el tablero
    if movida in tablero.juegoActual.movidas:
        # Ejecutar la jugada
        tablero.juegoActual = tablero.getResultado(tablero.juegoActual, movida)
        
        # Emitir el nuevo estado del juego
        emit('estado_juego', {'tablero': tablero.juegoActual.tablero, 'movidas': tablero.juegoActual.movidas}, broadcast=True)

    else:
        emit('error', {'mensaje': 'Movimiento inválido.'})

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5000)
