import socketio
from aiohttp import web
from core.datatools import namespaces
from django.core.management.base import BaseCommand
import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)

sio = socketio.AsyncServer(cors_allowed_origins='*', logger=logger)


@sio.event
def connect(sid):
    print(sid, 'connect')


class Command(BaseCommand):
    args = ''
    help = 'Подключение websocket'
    print('command')

    def handle(self, *args, **options):
        print('handler')
        app = web.Application()
        sio.attach(app)
        sio.register_namespace(namespaces.Chat('/chat/'))
        web.run_app(app)
