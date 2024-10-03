import websockets

try:
    ws = websockets.WebSocketServer()
    ws.connect("ws://localhost:5000/evento/")
    ws.send('evento', {'data': 'hola mundo'})
    print(ws.recv())
except websocket.WebSocket.ConnectionCloseException as e:
    print(e)