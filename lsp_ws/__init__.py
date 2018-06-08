import os
from io import BytesIO
import asyncio

from pyls.python_ls import PythonLanguageServer
from autobahn.asyncio.websocket import (
    WebSocketServerProtocol,
    WebSocketServerFactory,
)

__version__ = '0.1.0'

class WebsocketPylsWriterAdapter(object):
    """
    An adapter which has methods that `PythonLanguageServer`
    expects and it writes directly to the websocket client.
    """
    def __init__(self, client):
        self.client = client
        self._closed = False

    @property
    def closed(self):
        return self._closed

    def close(self):
        self._closed = True

    def write(self, data):
        self.client.sendMessage(data)
    
    def flush(self):
        pass


class LspWebsocketHandler(WebSocketServerProtocol):
    def onConnect(self, *args, **kwargs):
        self.pyls = None
        self.read_stream = None
        self.write_stream = None

    def onOpen(self):
        self.read_stream = BytesIO()
        self.write_stream = WebsocketPylsWriterAdapter(self)
        self.pyls = PythonLanguageServer(self.read_stream, self.write_stream)

    def onMessage(self, payload, is_binary):
        self.read_stream.truncate(0)
        self.read_stream.write(payload)
        self.read_stream.seek(0)
        self.pyls.start()

    def onClose(self, wasClean, code, reason):
        self.read_stream.close()
        self.write_stream.close()
        self.pyls = None


def start_server(host='0.0.0.0', port=2087, loop=None):
    factory = WebSocketServerFactory()
    factory.protocol = LspWebsocketHandler
    if not loop:
        loop = asyncio.get_event_loop()
    coroutine = loop.create_server(factory, host, port)
    server = loop.run_until_complete(coroutine)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.close()
        loop.close()
