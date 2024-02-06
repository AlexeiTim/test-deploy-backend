from channels.generic.websocket import AsyncWebsocketConsumer
import json
import socketio
from channels.consumer import AsyncConsumer


sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = socketio.ASGIApp(sio)


class YourConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({"type": "websocket.accept"})

    async def websocket_receive(self, text_data):
        await self.send({
            "type": "websocket.send",
            "text": "Hello from Django socket"
        })

    async def websocket_disconnect(self, event):
        pass

@sio.on('my event', namespace='/test')
async def test_message(sid, message):
    await sio.emit('my response', {'data': message['data']}, room=sid,
                   namespace='/test')


@sio.on('my broadcast event', namespace='/test')
async def test_broadcast_message(sid, message):
    await sio.emit('my response', {'data': message['data']}, namespace='/test')


@sio.on('join', namespace='/test')
async def join(sid, message):
    sio.enter_room(sid, message['room'], namespace='/test')
    await sio.emit('my response', {'data': 'Entered room: ' + message['room']},
                   room=sid, namespace='/test')


@sio.on('leave', namespace='/test')
async def leave(sid, message):
    sio.leave_room(sid, message['room'], namespace='/test')
    await sio.emit('my response', {'data': 'Left room: ' + message['room']},
                   room=sid, namespace='/test')


@sio.on('close room', namespace='/test')
async def close(sid, message):
    await sio.emit('my response',
                   {'data': 'Room ' + message['room'] + ' is closing.'},
                   room=message['room'], namespace='/test')
    await sio.close_room(message['room'], namespace='/test')


@sio.on('my room event', namespace='/test')
async def send_room_message(sid, message):
    await sio.emit('my response', {'data': message['data']},
                   room=message['room'], namespace='/test')


@sio.on('disconnect request', namespace='/test')
async def disconnect_request(sid):
    await sio.disconnect(sid, namespace='/test')


@sio.on('connect', namespace='/test')
async def test_connect(sid, environ):
    await sio.emit('my response', {'data': 'Connected', 'count': 0}, room=sid,
                   namespace='/test')


@sio.on('message')
async def print_message(sid, data):
    await sio.emit('new-message', {'data': 'message'})
    print(sid, data)


@sio.on('test')
def print_test(sid, env, data):
    print(data, 'test')



@sio.on('disconnect', namespace='/test')
def test_disconnect(sid):
    print('Client disconnected')