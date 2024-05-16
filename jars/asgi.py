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

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jars.settings')
print("DJANGO_SETTINGS_MODULE:", os.getenv('DJANGO_SETTINGS_MODULE'))
django.setup()
from manager.api import app as fastapi_app

django_app = get_asgi_application()

asgi_app = FastAPI()

asgi_app.mount("/api", fastapi_app)

asgi_app.mount("/", django_app)

application = asgi_app