# Import modules section
import re

from clean_console import *


# Function to create a new User.
def create_user():
    clear()

    # Insert data section.
    print("Define here the new user.", end="\n")
    name = input("Name: ")
    surname = input("Surname: ")
    address = input("Address: ")
    while True:
        phone_number = input("Phone number: ")

        # This pattern is used to validate the phone number.
        if re.match(r"^[-+]?\d{2,15}$", phone_number):
            break

    while True:
        print("Do you want to check data to be sure that's all correct?")
        check = input("Yes or No (y / n): ").lower()
        if check == "y":
            check_input(name, surname, address, phone_number)
        elif check == "n":
            break

    """# Creating a new instance "USER" to pass ad parameter to the proper function to be stored in a file.
    user = Classes.Users.User(name, surname, address, phone_number)

    # Function to store the new user in a file.
    Store_Data.Store_data.Store_Data_Into_Volume(user)"""


def check_input(name, surname, address, phone_number):
    print("\n")
    print("Here the info's defined.")
    print("Name: " + name)
    print("Surname: " + surname)
    print("Address: " + address)
    print("Phone Number: " + phone_number, end="\n\n")
    print("Is everything correct?")

    while True:
        correct = input("Yes or No (y / n): ").lower()
        if correct == "y":
            break
