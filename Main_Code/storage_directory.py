# Import modules section.
import os


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
