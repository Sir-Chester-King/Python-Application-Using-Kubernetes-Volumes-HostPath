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


def store_data(new_user_instance):
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
        with open(file_path, "ab") as file_users:

            # Serialize (pickle) the object and save it to the file.
            pickle.dump(new_user_instance, file_users)

        print("Data stored !!!")

    except FileNotFoundError:
        # Store the object in a file using pickle.
        # Open the file in binary write mode.
        with open(file_path, "wb") as file_users:

            # Serialize (pickle) the object and save it to the file.
            pickle.dump(new_user_instance, file_users)

        print("Data stored !!!")
    except PermissionError:
        print("You do not have permission to access this file.")
    except IOError:
        print("An I/O error occurred while writing the file.")
    except pickle.UnpicklingError as e:
        print(f"An unexpected error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
