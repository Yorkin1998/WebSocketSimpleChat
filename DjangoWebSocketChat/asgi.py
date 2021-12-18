"""
ASGI config for DjangoWebSocketChat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""
# sudo docker run -p 6379:6379 -d redis:2.8 
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoWebSocketChat.settings')

application = get_asgi_application()
