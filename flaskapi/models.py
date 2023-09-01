from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False) 
    created_at = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
    db.create_all()

