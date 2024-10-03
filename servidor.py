from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('evento')
def saludar(data):
    print("Mensaje : Recibido :", data)
    socketio.emit({'evento' : 'respuesta'})

if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)