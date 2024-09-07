import pickle
import re

from storage_directory import *
from view_data import load_all_user


# Destroy and create a new file.
# This because Pickle file creates an inconsistent data inside when you try to override it.
def empty_file():
    # Check or create the "Storage" directory.
    directory_storage_file = storage_directory()

    # Delete the file if it exists
    if os.path.exists(directory_storage_file):
        os.remove(directory_storage_file)

    try:
        # Recreate the file (empty)
        with open(directory_storage_file, 'wb') as file:
            pass  # This overrides the file into an empty file

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


# Modify a user's attribute object.
def modify_user():
    # If it wants to modify multiple users.
    loop_modify = True

    # Check or create the "Storage" directory.
    directory_storage_file = storage_directory()

    print("-" * 40)
    name_user = str(input("To modify the user, please insert the 'Name': "))

    # Load all users objects from the file to this "CLASS LIST"
    loaded_users = load_all_user()

    # Variable to check if there was any attribute change.
    change = False

    # Find the object with the specific "NAME"" and modify its attribute
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

    # No User found in the file.
    # Application terminate.
    if not change:
        print("User not found.")
        return 0

    # Wipe the file to be overridden.
    empty_file()

    # Writing the data in the file.
    # Write one object of the list per time.
    for override_data in loaded_users:
        try:
            # Store the object in a file using pickle.
            # Open the file in binary write mode.
            with open(directory_storage_file, "ab") as file_users:

                # Serialize (pickle) the object and save it to the file.
                pickle.dump(override_data, file_users)

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
    print("Data stored !!!")
