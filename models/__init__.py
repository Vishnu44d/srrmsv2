from .meta import Base

def createTables(engine):
    Base.metadata.create_all(engine)

def destroyTables(engine):
    Base.metadata.drop_all(engine)