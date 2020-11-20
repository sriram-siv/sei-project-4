"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat_messages.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# application = get_wsgi_application()

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'http': get_wsgi_application(),
    'https': get_wsgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat_messages.routing.websocket_urlpatterns
        )
    ),
})
