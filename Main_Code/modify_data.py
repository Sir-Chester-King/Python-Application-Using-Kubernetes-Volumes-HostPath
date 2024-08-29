import re

from view_data import *


def modify_user():
    # If it wants to modify multiple users.
    loop_modify = True

    # Check or create the "Storage" directory.
    directory_storage = storage_directory()

    # The Name of the file will contain the user's data.
    # Using PICKLE Serializing.
    file_name_storage = "Users_Data.pkl"

    # Path of the txt file where the user's data will stored
    file_path = os.path.join(directory_storage, file_name_storage)

    print("-" * 40)
    name_user = str(input("To modify the user, please insert the 'Name': "))

    # Load all users objects from the file to this "CLASS LIST"
    loaded_users = load_all_user()

    print("TYPESSSS: ", type(loaded_users))

    for users in loaded_users:
        print("Name:", users.get_name())
        print("Surname:", users.get_surname())
        print("Address:", users.get_address())
        print("Phone Number:", users.get_phone_number())
        print("-" * 40)

    change = None

    # Find the object with the specific name and modify its attribute
    for user in loaded_users:
        if str(user.get_name()) == name_user:
            user.set_name(input("Name: "))
            user.set_surname(input("Surname: "))
            user.set_address(input("Address: "))

            while True:
                phone_number = input("Phone number: ")

                # This pattern is used to validate the phone number.
                if re.match(r"^[-+]?\d{2,15}$", phone_number):
                    user.set_phone_number(phone_number)
                    break
            change = True

        if not change:
            print("User not found.")
            return 0

    # Writing the data in the file.
    try:
        # Store the object in a file using pickle.
        # Open the file in binary write mode.
        with open(file_path, "wb") as file_users:

            # Serialize (pickle) the object and save it to the file.
            pickle.dump(loaded_users, file_users)

        print("Data stored !!!")

        print("TYPE:", type(loaded_users))

    except FileNotFoundError:
        print("File not found")
    except PermissionError:
        print("You do not have permission to access this file.")
    except IOError:
        print("An I/O error occurred while writing the file.")
    except pickle.UnpicklingError as e:
        print(f"An unexpected error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    """# Writing the data in the file.
    try:
        # Store the object in a file using pickle.
        # Open the file in binary write mode.
        with open(file_path, "wb") as file_users:

            # Serialize (pickle) the object and save it to the file.
            pickle.dump(loaded_users, file_users)

        print("Data stored !!!")

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("You do not have permission to access this file.")
    except IOError:
        print("An I/O error occurred while writing the file.")
    except pickle.UnpicklingError as e:
        print(f"An unexpected error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")"""
