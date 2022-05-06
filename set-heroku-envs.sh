#!bin/bash
heroku addons:create heroku-postgresql:hobby-dev

heroku config:set FLASK_APP=webapp.py

python3 -c "import uuid ; sec_key=uuid.uuid4().hex"


heroku config:set SECRET_KEY=sec_key

heroku config:set FLASK_ENV=heroku

heroku config:set MAIL_USERNAME=anabantiakachi1@gmail.com
heroku config:set MAIL_PASSWORD=@g00gle.c0m.c0m

