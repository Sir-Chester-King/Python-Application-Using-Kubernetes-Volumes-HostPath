# Import modules section
import pickle
import re

from Classes.user_class import User
from clean_console import *


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


# Check the validate input
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
            check_value = True  # All info are correct.
            break  # Break the loop.

        elif correct == "n":
            break  # Break the loop, without changing the check_value variable (FALSE as default).

    if check_value:
        return True  # Input ARE correct.
    else:
        return False  # Input are NOT correct.


# Function to check if the "Storage" directory exist or not.
# If not, it will be created.
def storage_directory():
    # This is the PATH inside the Project Directory (current directory)
    absolute_path = os.path.abspath(__file__)

    # Go up one level
    one_level_up = os.path.dirname(absolute_path)

    # Go up two levels
    two_level_up = os.path.dirname(one_level_up)

    # Path of the "Storage" directory.
    directory_storage = os.path.join(two_level_up, "Storage")

    # Check if the directory inside the project exist or not.
    # In case it doesn't exist, it is created.
    if not os.path.exists(directory_storage):
        os.makedirs(directory_storage)
        print(f"Created directory: {directory_storage}")

    return directory_storage


# Function to create a new User.
def create_user():
    name, surname, address, phone_number = None, None, None, None

    # False as default for not correct info inserted.
    correct_user_insert = False

    while not correct_user_insert:
        clear()
        name, surname, address, phone_number = ask_data()

        while True:
            print("Do you want to check data to be sure that's all correct?")
            check = input("Yes or No (y / n): ").lower()

            if check == "y":
                check_value = check_input(name, surname, address, phone_number)

                # Input ARE correct.
                if check_value:
                    correct_user_insert = True
                    break  # Break the loop.
                else:
                    break  # Break the loop, without changing the correct_user_insert variable (FALSE as default).

            elif check == "n":
                correct_user_insert = True
                break

    # Creating a new instance "USER" to pass ad parameter to the proper function to be stored in a file.
    new_user_instance = User(name, surname, address, phone_number)

    # Check or create the "Storage" directory.
    directory_storage = storage_directory()

    # Name of the file will contain the user's data.
    # Using PICKLE Serializing.
    file_name_storage = "Users_Data.pkl"

    # Path of the txt file where the user's data will stored
    file_path = os.path.join(directory_storage, file_name_storage)

    # Writing the data in the file.
    try:
        # Store the object in a file using pickle.
        # Open the file in binary write mode.
        with open(file_path, "wb") as file:

            # Serialize (pickle) the object and save it to the file.
            pickle.dump(new_user_instance, file)
    except FileNotFoundError:
        # Store the object in a file using pickle.
        # Open the file in binary write mode.
        with open(file_path, "wb") as file:

            # Serialize (pickle) the object and save it to the file.
            pickle.dump(new_user_instance, file)
    except PermissionError:
        print("You do not have permission to access this file.")
    except IOError:
        print("An I/O error occurred while writing the file.")
    except pickle.UnpicklingError as e:
        print(f"An unexpected error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Open the file in binary read mode.
    with open(file_path, 'rb') as file:

        # Deserialize (unpickle) the object from the file
        loaded_data = pickle.load(file)
    print("Read", loaded_data)


create_user()
