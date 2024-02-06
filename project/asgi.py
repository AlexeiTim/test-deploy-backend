import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
django_asgi_app = get_asgi_application()

import core.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket":
        URLRouter(
            core.routing.websocket_urlpatterns
        ),
})

app = application
