import socketio


class Chat(socketio.AsyncNamespace):
    """Namespace для чата."""

    async def on_connect(self, sid: str, environ: dict, auth: dict):
        print('connect', sid,' hahshshsh')

