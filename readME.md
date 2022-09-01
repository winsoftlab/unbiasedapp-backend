pip install -r requirements.txt

create a .env file in the root folder

store the TWITTER_KEY and TWITTER_SECRET in the .env file
set the FLASK_APP = webapp.py

set SECRET_KEY. FACEBOOK_APP_ID and FACEBOOK_APP_SECRET

set the appropriate FLASK_ENV environment

execute the ''flask init db'' command

execute ''flask db migrate''

execute "flask db upgrade"

execute "flask run --cert=adhoc" for localhost

technical ISSUE :facebook_scraper module has been disabled. This a general problem.
    Consequence: Reimplemantation of Facebook Graph API for page acess_token to get comments made on page

