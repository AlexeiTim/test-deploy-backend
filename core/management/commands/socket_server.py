import socketio
from aiohttp import web
from core.datatools import namespaces
from django.core.management import BaseCommand

sio = socketio.AsyncServer(cors_allowed_origins='*')


class Command(BaseCommand):
    args = ''
    help = 'Подключение websocket'
    print('command')

    def handle(self, *args, **options):
        print('handler')
        app = web.Application()
        sio.attach(app)

        @sio.event
        async def message(sid, data):
            await sio.emit('new_message', {'message': 'Yep, I received your message'}, to=sid)
            print(data)
            return 'HELLO!!!'
        # sio.register_namespace(namespaces.Chat('/chat/'))
        web.run_app(app)
