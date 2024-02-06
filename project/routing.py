# # mysite/routing.py
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# import core.routing
# from core.consumers import app
# from django.core.asgi import get_asgi_application
#
# django_asgi_app = get_asgi_application()
#
# application = ProtocolTypeRouter({
#     # (http->django views is added by default)
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             core.routing.websocket_urlpatterns
#         )
#     ),
# })
