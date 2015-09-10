"""
WSGI config for deskxd_com project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

path = '/home/active/Django_deskxd.com'
if path not in sys.path:
        print "====== Not in! ======"
        sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deskxd_com.settings")

application = get_wsgi_application()
