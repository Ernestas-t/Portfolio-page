from django.apps import AppConfig
from django.conf import settings
import sys
from urllib.parse import urlparse

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
