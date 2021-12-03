"""
WSGI config for suppliers project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'suppliers.settings')
# application = get_wsgi_application()


###################### Lisätty ####################################

# If WEBSITE_HOSTNAME is defined as an environment variable, then we're running
# on Azure App Service and should use the production settings in production.py.
settings_module = "suppliers.production" if 'WEBSITE_HOSTNAME' in os.environ else 'suppliers.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
######################################################################

application = get_wsgi_application()
