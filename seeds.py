from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from tables import *

DATABASE_URL = 'sqlite:///database.db'

engine= create_engine(DATABASE_URL)

BASE = declarative_base()

session = sessionmaker(bind=engine)
Session = session()

#HOTELS
Hotel1 = Hotel(name ="Nigel Peaks Nairobi",adress = 5660)
Hotel2 = Hotel(name="Nigel peaks Eldoret",adress = 3450)
Hotel3 = Hotel(name="Nigel peaks Mombasa",adress = 4000)
#ROOM
Room1 = Room (number = 1,room_type = "single",Hotel_adress= 5660)
Room2 = Room (number = 2,room_type = "double",Hotel_adress=3450)
Room3 = Room (number= 2,room_type = "single",Hotel_adress = 4000)
#GUESTS
Guests1 = Guest(phone_number = ("254724064757"),email = "nigelboke@gmail.com",passkey= 1/5660,room_id= "h156")
Guests2 = Guest(phone_number=("25472345674747"), email= "kingpepe@gmail.com",passkey=2/3450,room_id ="h234")
Guests3 = Guest(phone_number=("072944959585"),email ="tululu@gmail.com",passkey=3/4000, room_id ="h340")




Session.add_all([Hotel1,Hotel2,Hotel3,Room1,Room2,Room3,Guests1,Guests2,Guests3])
Session.commit()
Session.close()


