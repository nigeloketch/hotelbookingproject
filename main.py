from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from tables import *

DATABASE_URL = 'sqlite:///database.db'

engine = create_engine(DATABASE_URL)

BASE = declarative_base()

Session = sessionmaker(bind=engine)

def main():
    print("Hotel Booking System")
    while True:
        print("1. Sign In")
        print("2. Exit")
        choice = input("Enter your choice (1/2): ")
        
        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            
            # Query the database to check if the user exists
            session = Session()
            user = session.query(Guest).filter_by(email=username, passkey=password).first()
            session.close()
            
            if user:
                print(f"Welcome, {user.email}!")
                address = input("Enter the address of the hotel: ")
                HotelList = session.query(Hotel)
                print(f"Welcome to {address} - Hotels: {HotelList.count()}")
            else:
                print("Invalid username or password.")
               
        elif choice == "2":
            print("Have a splendid day")
            break
        else:
            print("Invalid choice. Please try again.")

    print("Thank you for using choosing us!")
    

def fill_guest_details():
    try:
        # Get user input
        phone_number = input("Enter phone number: ")
        email = input("Enter email address: ")
        passkey = input("Enter passkey: ")
        room_id = int(input("Enter room ID: "))  # Assuming room ID is an integer

        # Create a new guest instance and add it to the database
        guest = Guest(phone_number=phone_number, email=email, passkey=passkey, room_id=room_id)
        
        session = Session()
        session.add(guest)
        session.commit()
        session.close()

        print("Welcome to Nigel Hotels!")

    except Exception as e:
        print(f"Error: {str(e)}")


def main():
    print("Hotel Booking System - Room Booking Page")
    
    # List available hotels
    session = Session()
    hotels = session.query(Hotel).all()
    
    if not hotels:
        print("No hotels available.")
        return
    
    print("Available Hotels:")
    for i, hotel in enumerate(hotels, start=1):
        print(f"{i}. {hotel.name}")
    
    try:
        # Get user input for hotel selection
        hotel_choice = int(input("Select a hotel (1, 2, 3): "))
        selected_hotel = hotels[hotel_choice - 1]
        
        # List available rooms for the selected hotel
        available_rooms = session.query(Room).filter_by(Hotel_adress=selected_hotel.adress).all()
        
        if not available_rooms:
            print(f"No available rooms at {selected_hotel.name}.")
            return
        
        print("Available Rooms:")
        for i, room in enumerate(available_rooms, start=1):
            print(f"{i}. Room {room.number} - {room.room_type}")
        
        # Get user input for room selection
        room_choice = int(input("Select a room (1, 2, 3): "))
        selected_room = available_rooms[room_choice - 1]
        
        # Get user details
        phone_number = input("Enter your phone number: ")
        email = input("Enter your email address: ")
        passkey = input("Enter a passkey: ")
        
        # Create a new guest instance
        guest = Guest(phone_number=phone_number, email=email, passkey=passkey, room_id=selected_room.id)
        
        # Add the guest to the database
        session.add(guest)
        session.commit()
        
        print("Room booking successful!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except IndexError:
        print("Invalid selection. Please select from the available options.")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        session.close()


if __name__ == "__main__":
    fill_guest_details()

if __name__ == "__main__":
    main()



