from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime, Table, ForeignKeyConstraint, Boolean
from .meta import Base
#from flask_bcrypt import Bcrypt
import datetime


class Passenger(Base):
	"""A user after he/she has booked a ticket"""
	
	__tablename__ = "passenger"

	pnr = Column(String(20), primary_key = True )
	p_name = Column(String(20), nullable = False )
	reserve_status = Column(Boolean,nullable= False  )
	age = Column(String(5), nullable = False )
	gender = Column(String(10), nullable = True)
	seat_no = Column(String(5),nullable=False)
	start_sid = Column(String(20),nullable=False)
	end_sid = Column(String(20),nullable=False)
	
	
class Book1(Base):
	__tablename__ = "Book1"
	pnr = Column(String(20), primary_key = True )
	user_id = Column(String(20), primary_key = True )
	train_id = Column(String(20) , primary_key = True )
	#status_id = Column(String(20), primary_key = True )
	
	

class Book2(Base):
	__tablename__ = "Book2"
	pnr = Column(String(20), primary_key = True )
	date = Column(DateTime , nullable = False)
	