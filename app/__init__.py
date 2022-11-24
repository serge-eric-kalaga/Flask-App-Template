from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restx import Api
from .routes import api
from .models import db
from .config import Config


def create_app(config=Config):
    
    app = Flask(__name__)
    
    app.config.from_object(config)
    
    db.init_app(app)
    
    api.init_app(app)
    
    jwt = JWTManager(app)
    
    with app.app_context():
        from .models.utilisateur import Utilisateur
        db.create_all()
        try :
            user = Utilisateur("serge", "1234", "kalagaserge4@gmail.com")
            user.save()
        except : pass
    
    return app