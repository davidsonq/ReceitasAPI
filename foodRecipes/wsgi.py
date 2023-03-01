"""
WSGI config for foodRecipes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodRecipes.settings')
sys.path.append('/var/www/ReceitasAPI')
sys.path.append('/var/www/ReceitasAPI/foodRecipes')

application = get_wsgi_application()
