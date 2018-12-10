from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime, Table, ForeignKeyConstraint, Boolean
from .meta import Base
from flask_bcrypt import Bcrypt
import datetime
from SRRMSv2.config import key
import jwt

db = SQLAlchemy()
flask_bcrypt = Bcrypt()

class User(Base):
    """ User Model for storing user related details """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    registered_on = Column(DateTime, nullable=False)
    admin = Column(Boolean, nullable=False, default=False)
    public_id = Column(String(100), unique=True)
    username = Column(String(50), unique=True)
    password_hash = Column(String(100))
    
    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)


    def __repr__(self):
        return "<User '{}'>".format(self.username)
