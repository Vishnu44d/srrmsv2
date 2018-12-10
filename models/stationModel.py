from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime, Table, ForeignKeyConstraint, Boolean
from .meta import Base
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class Station(Base):
	__tablename__ = "station"

	station_id = Column(String(20) , primary_key = True)
	station_name = Column(String(20) , nullable = False)

class ConsistsOf(Base):
	__tablename__ = "route_consists_of"
	
	station_id = Column(String(20) , primary_key = True)
	train_id = Column(String(20) , primary_key = True)
	stop_no = Column(String(3) , primary_key = True)