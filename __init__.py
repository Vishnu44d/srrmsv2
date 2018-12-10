from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy_utils.functions import create_database, database_exists
from .config import DevelopmentConfig

def create_db_engine(config):
    if(not database_exists(config.SQLALCHEMY_DATABASE_URI)):
        create_database(config.SQLALCHEMY_DATABASE_URI)
    engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
    return engine

def create_db_sessionFactory(engine):
    sessionFactory = sessionmaker(bind=engine, expire_on_commit=False)
    return sessionFactory
