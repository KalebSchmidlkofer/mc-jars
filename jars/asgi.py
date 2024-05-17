"""
ASGI config for jars project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from fastapi import FastAPI


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jars.settings')

print("DJANGO_SETTINGS_MODULE:", os.getenv('DJANGO_SETTINGS_MODULE'))
django.setup()
from manager.api import app as fastapi_app

django_app = get_asgi_application()

asgi_app = FastAPI()

asgi_app.mount("/api", fastapi_app)

asgi_app.mount("/", django_app)

application = asgi_app



class DjangoAuthMiddleware:
    def __init__(self):
        self.get_user = django.contrib.auth.get_user_model()

    async def __call__(self, request, call_next):
        django_request = django.core.handlers.asgi.get_asgi_request(request)
        django_request.user = await self.get_user(django_request)
        response = await call_next(request)
        return response


# Attach Django Authentication Middleware
# asgi_app.add_middleware(DjangoAuthMiddleware)