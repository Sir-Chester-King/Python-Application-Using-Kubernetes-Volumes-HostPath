# Import modules section.
import pickle

from storage_directory import *

"""
    WATCH OUT !!! PICKLE MODULE IS NOT SECURE, IT BE USED AS EDUCATION PURPOSE

    Only unpickle data you trust.
    It is possible to construct malicious pickle data which will execute arbitrary code during unpickling. 
    Never unpickle data that could have come from an untrusted source, or that could have been tampered with.

    FOR MORE DETAIL: https://docs.python.org/3/library/pickle.html
"""


def list_all_users():
    # Check or create the "Storage" directory.
    directory_storage = storage_directory()

    # The Name of the file will contain the user's data.
    # Using PICKLE Serializing.
    file_name_storage = "Users_Data.pkl"

    # Path of the txt file where the user's data will stored
    file_path = os.path.join(directory_storage, file_name_storage)

    loaded_data_users = []

    try:
        # Open the file in binary read mode.
        with open(file_path, 'rb') as file_users:
            while True:
                try:
                    # Deserialize (unpickle) the object from the file
                    loaded_data = pickle.load(file_users)
                    print("DIR: ", dir(loaded_data))

                    # Insert the object read into a list.
                    loaded_data_users.append(loaded_data)

                # Keep loop until read all the file.
                except EOFError:
                    break
    except PermissionError:
        print("You do not have permission to access this file.")
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An I/O error occurred while writing the file.")
    except pickle.UnpicklingError as e:
        print(f"An unexpected unpickling error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    print("-" * 40)
    print("TYPE:", type(loaded_data_users))
    # Print the LIST of all users (read from the binary file).

    for users in loaded_data_users:
        print("Name:", users.get_name())
        print("Surname:", users.get_surname())
        print("Address:", users.get_address())
        print("Phone Number:", users.get_phone_number())
        print("-" * 40)

    print("All objects have been loaded and their attributes printed.")


def load_all_user():
    # Check or create the "Storage" directory.
    directory_storage = storage_directory()

    # The Name of the file will contain the user's data.
    # Using PICKLE Serializing.
    file_name_storage = "Users_Data.pkl"

    # Path of the txt file where the user's data will stored
    file_path = os.path.join(directory_storage, file_name_storage)

    loaded_data_users = []

    try:
        # Open the file in binary read mode.
        with open(file_path, 'rb') as file_users:
            while True:
                try:
                    # Deserialize (unpickle) the object from the file
                    loaded_data = pickle.load(file_users)

                    # Ensure we have a list
                    if not isinstance(loaded_data, list):
                        raise ValueError("Loaded data is not a list")

                    # Insert the object read into a list.
                    loaded_data_users.append(loaded_data)

                # Keep loop until read all the file.
                except EOFError:
                    break
    except PermissionError:
        print("You do not have permission to access this file.")
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An I/O error occurred while writing the file.")
    except pickle.UnpicklingError as e:
        print(f"An unexpected unpickling error occurred: {e}")
    except EOFError:
        print("Error loading data. Returning an empty list.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return loaded_data_users
