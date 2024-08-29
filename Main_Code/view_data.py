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

    # Name of the file will contain the user's data.
    # Using PICKLE Serializing.
    file_name_storage = "Users_Data.pkl"

    # Path of the txt file where the user's data will stored
    file_path = os.path.join(directory_storage, file_name_storage)

    try:
        # Open the file in binary read mode.
        with open(file_path, 'rb') as file_users:
            # Deserialize (unpickle) the object from the file
            loaded_data_users = pickle.load(file_users)

        print("Name:", loaded_data_users.get_name())
        print("Surname:", loaded_data_users.get_surname())
        print("Address:", loaded_data_users.get_address())
        print("Phone Number:", loaded_data_users.get_phone_number())
    except PermissionError:
        print("You do not have permission to access this file.")
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An I/O error occurred while writing the file.")
    except pickle.UnpicklingError as e:
        print(f"An unexpected error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
