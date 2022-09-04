import datetime
from flask import current_app, url_for
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from .extensions import db, login_manger
from werkzeug.security import generate_password_hash, check_password_hash

class StripeCustomer(db.Model):
    __tablename__ = 'stripe_customer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    StripeCustomerId = db.Column(db.String(255), nullable=False)
    StripeSubscriptionId = db.Column(db.String(255), nullable = False, unique=True)

class TwitterAnalysis(db.Model):
    __tablename__ = 'twitter_analysis'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    search_query= db.Column(db.String(255), nullable=False, unique=True)
    sentiments = db.Column(db.String)


class FacebookAnalysis(db.Model):
    __tablename__ = 'facebook_analysis'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    search_query= db.Column(db.String(255), nullable=False, unique=True)
    sentiments = db.Column(db.String)

class AmazonAnalysis(db.Model):
    __tablename__ = 'amazon_analysis'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_info = db.Column(db.String(255), nullable=False)
    sentiments = db.Column(db.String)


class InstagramAnalysis(db.Model):
    __tablename__ = 'instagram_analysis'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    search_query = db.Column(db.String(255), nullable=False, unique=True, default='comments')
    sentiments = db.Column(db.String)


class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=True)
    fb_access_token = db.Column(db.String)
    fb_page_id = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_confirmation_token(self, expiration=7200):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({ 'confirm':self.id }).decode('utf-8')

    def confirm(self, token):
        s= Serializer(current_app.config['SECRET_KEY'])
        try:
            data=s.loads(token.encode('utf-8'))
        except:
            return False

        if data.get('confirm') != self.id:
            return False

        self.confirmed = True
        db.session.add(self)
        return True
    
    def generate_auth_token(self, expiration):
        s = Serializer(current_app.config['SECRET_KEY'],
                            expires_in=expiration)
        return s.dumps({'id':self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])

@login_manger.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

