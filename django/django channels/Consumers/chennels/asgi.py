"""
ASGI config for chennels project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chennels.settings')

from channels.routing import ProtocolTypeRouter #recive a request and send to the requested protocol
from channels.routing import URLRouter
import websocket.routing
application = ProtocolTypeRouter({
  'http' : get_asgi_application(), 
  'websocket' : URLRouter(
    websocket.routing.websocket_urlpatterns
  )
})
