release: python manage.py migrate
web: gunicorn -w 4 project.wsgi application
worker: python manage.py send_mail