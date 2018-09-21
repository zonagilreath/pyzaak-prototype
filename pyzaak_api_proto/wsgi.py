"""
WSGI config for pyzaak_api_proto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'pyzaak_api_proto.settings.prod')

application = DjangoWhiteNoise(get_wsgi_application())
