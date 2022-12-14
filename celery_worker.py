import os

from app import create_app

app = create_app(os.environ.get("FLASK_CONFIG") or 'default')

app.app_context().push()


from app import celery_app