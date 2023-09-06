#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from os import path

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    """
    """
    app = Flask(__name__)
    # app.config['ENV'] = os.environ.get('ENV')
    # app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    # app.config['STATIC_FOLDER'] = 'static'
    app.config['SECRET_KEY'] = '1234'
    
    # db.init_app(app)
    # migrate.init_app(app)
    # login_manager.init_app(app)

    from .auth import auth
    app.register_blueprint(auth, url_prefix="/")
    from .views import views
    app.register_blueprint(views, url_prefix="/")

    # from .model import *

    # @login_manager.user_loader
    # def load_user(user_id):
    #     return User.get(user_id)
    

    # with app.app_context():
    #     db.create_all()

    return app
