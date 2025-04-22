from hotel_functions import *

def main():
    while True:
        print("\nMenu:")
        print("1. Add a hotel")
        print("2. Delete a hotel")
        print("3. Update hotel rating")
        print("4. View all hotels")
        print("5. Search hotels")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_hotel()
        elif choice == "2":
            delete_hotel()
        elif choice == "3":
            update_rating()
        elif choice == "4":
            view_hotels()
        elif choice == "5":
            search_hotels()
        elif choice == "6":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
