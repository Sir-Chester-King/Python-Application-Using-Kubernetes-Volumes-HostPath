# Import modules section.
import re

from Classes.user_class import User
from clean_console import *
from store_data import store_data


# Function to gather the user's input.
def ask_data():

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

    return name, surname, address, phone_number


# Check and validate the input.
def check_input(name, surname, address, phone_number):
    # False as default for not correct info inserted.
    check_value = False

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
            check_value = True  # All info is correct.
            break  # Break the loop.

        elif correct == "n":
            break  # Break the loop, without changing the check_value variable (FALSE as default).

    if check_value:
        return True  # Input IS correct.
    else:
        return False  # Input is NOT correct.


# Function to create a new User.
def create_user():
    name, surname, address, phone_number = None, None, None, None

    # False as default for not correct info inserted.
    correct_user_insert = False

    # Loop if there wer no correct inserted user's info.
    while not correct_user_insert:
        clear()

        # Call the function to ask in input the user's info.
        name, surname, address, phone_number = ask_data()

        while True:
            print("Do you want to check data to be sure that's all correct?")
            check = input("Yes or No (y / n): ").lower()

            if check == "y":
                check_value = check_input(name, surname, address, phone_number)

                # Input "IS" correct.
                if check_value:
                    correct_user_insert = True
                    break  # Break the loop.
                else:
                    break  # Break the loop, without changing the correct_user_insert variable (FALSE as default).

            # The user chose to do not check and validate the input.
            elif check == "n":
                correct_user_insert = True
                break

    # Creating a new instance "USER" to pass ad parameter to the proper function to be stored in a file.
    new_user_instance = User(name, surname, address, phone_number)

    # Call the "store_data" function.
    store_data(new_user_instance)
