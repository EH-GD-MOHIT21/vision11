"""
ASGI config for vision11 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

import chatsupportAPP.sockets.routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vision11.settings')
get_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_app,
    'websocket': AuthMiddlewareStack( 
        URLRouter(
        chatsupportAPP.sockets.routing.websocket_urlpatterns
    )
    ),
})
