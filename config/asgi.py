

import os
from django.urls import path
from home.consumers import TestConsumer,NewConsumer
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

application = get_asgi_application()


ws_patterns = [
    path('test/', TestConsumer.as_asgi()),
    path('test/app/', NewConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(ws_patterns),
    'http': get_asgi_application(),
    })