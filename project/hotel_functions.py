import json
import os

FILE_PATH = "hotels.json"

def load_hotels():
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            json.dump([], f)
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_hotels(hotels):
    with open(FILE_PATH, "w") as f:
        json.dump(hotels, f, indent=4)

def add_hotel():
    hotels = load_hotels()
    try:
        hotel_id = int(input("Enter hotel ID: "))
        for hotel in hotels:
            if hotel["ID"] == hotel_id:
                print("Hotel with this ID already exists.")
                return
        name = input("Enter hotel name: ")
        location = input("Enter hotel location: ")
        rating = float(input("Enter hotel rating: "))
        hotel = {"ID": hotel_id, "name": name, "location": location, "rating": rating}
        hotels.append(hotel)
        save_hotels(hotels)
        print("Hotel added successfully!")
    except ValueError:
        print("Invalid input. Please enter correct data types.")

def delete_hotel():
    hotels = load_hotels()
    try:
        hotel_id = int(input("Enter hotel ID to delete: "))
        hotels = [h for h in hotels if h["ID"] != hotel_id]
        save_hotels(hotels)
        print("Hotel deleted successfully!")
    except ValueError:
        print("Invalid ID.")

def view_hotels():
    hotels = load_hotels()
    if not hotels:
        print("No hotels available.")
    else:
        for hotel in hotels:
            print(f"ID: {hotel['ID']}, Name: {hotel['name']}, Location: {hotel['location']}, Rating: {hotel['rating']}")

def update_rating():
    hotels = load_hotels()
    try:
        hotel_id = int(input("Enter hotel ID to update rating: "))
        found = False
        for hotel in hotels:
            if hotel["ID"] == hotel_id:
                new_rating = float(input("Enter new rating: "))
                hotel["rating"] = new_rating
                found = True
                break
        if found:
            save_hotels(hotels)
            print("Rating updated successfully!")
        else:
            print("Hotel not found.")
    except ValueError:
        print("Invalid input.")

def search_hotels():
    hotels = load_hotels()
    try:
        hotel_id = int(input("Enter hotel ID to search: "))
        found = False
        for hotel in hotels:
            if hotel["ID"] == hotel_id:
                print(f"ID: {hotel['ID']}, Name: {hotel['name']}, Location: {hotel['location']}, Rating: {hotel['rating']}")
                found = True
                break
        if not found:
            print("Hotel not found.")
    except ValueError:
        print("Invalid ID.")