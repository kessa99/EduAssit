#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from os import path

load_dotenv()

db = SQLAlchemy()
DB_NAME = "database.db"
migrate = Migrate()
login_manager = LoginManager()


def create_database(app):
    with app.app_context():
        if not path.exists("eduassit/" + DB_NAME):
            db.create_all()
            print("Created database!")

def create_app():
    """
    """
    app = Flask(__name__)
    # app.config['ENV'] = os.environ.get('ENV')
    # app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    app.config['SECRET_KEY'] = '1234'
    
    
    migrate.init_app(app, db)
    # login_manager.init_app(app)

    from .auth import auth
    app.register_blueprint(auth, url_prefix="/")
    from .views import views
    app.register_blueprint(views, url_prefix="/")

    create_database(app)

    from .model import User, Community
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

    return app

