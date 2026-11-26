import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lost_and_found_project.settings")

application = get_wsgi_application()
