from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime, Table, ForeignKeyConstraint, Boolean
from .meta import Base
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


db = SQLAlchemy()

class TrainStatus(Base):
	
	__tablename__ = "train_status"
	
	status_id = Column(String(10) , primary_key = True )
	wait_seat = Column(Integer , nullable = False )
	available_seat = Column(Integer , nullable = False)
	#train_id = Column(Integer , nullable = False , unique = True)
	train_id = relationship(Train , backref= 'TrainStatus')
	

class Train(Base):
	
	__tablename__ = "train"
	
	train_id = Column(String(20) , primary_key = True)
	train_name = Column(String(20) , nullable = False)
	train_type = Column(String(20) , nullable = False )
	
class TrainSpec(Base):
	__tablename__ = "TrainSpec"
	
	train_id = Column(String(20) , primary_key = True)
	start_sid = Column(String(20) , primary_key = True)
	end_sid = Column(String(20) , primary_key = True)
	