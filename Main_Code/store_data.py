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


# Function to store the user object instance in the Pickle binary file.
def store_data(new_user_instance):
    # Check or create the "Storage" directory.
    directory_storage_file = storage_directory()

    # Writing the data in the file.
    try:
        # Store the object in a file using pickle.
        # Open the file in binary APPEND mode.
        with open(directory_storage_file, "ab") as file_users:

            # Serialize (pickle) the object and save it to the file.
            pickle.dump(new_user_instance, file_users)

    except FileNotFoundError:  # Create a new pickle binary file.

        # Store the object in a file using pickle.
        # Open the file in binary WRITE mode.
        with open(directory_storage_file, "wb") as file_users:

            # Serialize (pickle) the object and save it to the file.
            pickle.dump(new_user_instance, file_users)

    except PermissionError:
        print("You do not have permission to access this file.")
    except IOError:
        print("An I/O error occurred while writing the file.")
    except pickle.UnpicklingError as e:
        print(f"An unexpected error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
