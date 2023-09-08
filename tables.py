from sqlalchemy import create_engine, Column, Integer, String  # Import String for VARCHAR
from sqlalchemy.orm import declarative_base,sessionmaker

DATABASE_URL = 'sqlite:///database.db'

engine = create_engine(DATABASE_URL)

BASE = declarative_base()

session = sessionmaker(bind=engine)
Session = session()

class Hotel(BASE):  # Class name should start with an uppercase letter
    __tablename__ = 'Hotel'
    id = Column(Integer, primary_key=True)
    name = Column(String)  # Specify the length of VARCHAR if needed, e.g., String(255)
    adress = Column(String)  

class Room(BASE):  
    __tablename__ = 'Room'
    id = Column(Integer, primary_key=True)
    number = Column(String, nullable=False)  # Use String for VARCHAR
    room_type = Column(Integer)
    Hotel_adress = Column(Integer,nullable=True)

    

class Guest(BASE):  # Class name should start with an uppercase letter
    __tablename__ = 'Guests'
    id = Column(Integer, primary_key=True)
    phone_number = Column(Integer, nullable=False)  # Use String for phone numbers if needed
    email = Column(String, nullable=False)  # Use String for email addresses
    passkey = Column(String, nullable=False)  # Use String for passwords if needed
    room_id = Column(Integer, nullable=False)


BASE.metadata.create_all(bind = engine)
Session.commit()
Session.close()

