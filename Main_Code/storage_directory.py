# Import modules section.
import os
from pathlib import Path


# Function to check if the "Storage" directory exist or not.
# If not, it will be created.
def storage_directory():
    path_storage = Path(os.getenv("Path_Storage"))  # Environment variable gather form Dockerfile.
    name_file_storage = Path(os.getenv("Name_File_Storage"))  # Environment variable gather form Dockerfile.

    # Check if the directory inside the project exists or not.
    # In case it doesn't exist, it is created.
    if not os.path.exists(path_storage):
        os.makedirs(path_storage)
        print(f"Created directory: {path_storage}")

    # Path of the "Storage" directory.
    directory_container_storage = path_storage / name_file_storage

    return directory_container_storage
