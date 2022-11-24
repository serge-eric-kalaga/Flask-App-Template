from . import db
from werkzeug.security import generate_password_hash

class Utilisateur(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    is_delete = db.Column(db.Boolean(), default=False)
    
    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        
    def getAll():
        return Utilisateur.query.filter_by(is_delete=False)
    
    def getOne(username):
        return Utilisateur.query.filter_by(username=username).first_or_404()
    
    def delete(username):
        to_del = Utilisateur.query.filter_by(username=username).first()
        db.session.delete(to_del)
        db.session.commit()
    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def edit(self, username=None, password=None, email=None):
        if username is not None : self.username = username
        if password is not None : self.password = password
        if email is not None : self.email = email
        
        db.session.add(self)
        db.session.commit()