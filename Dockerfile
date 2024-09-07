FROM python:latest

# Attributes for MetaData
LABEL authors = "Nicola Ricciardi"

# Work directory for the container.
WORKDIR /Docker_Directory

# Copy all the file in the current directory of the project, in the specified Workdir.
COPY . .

# Set the PYTHONPATH enviroment variable, to include the "Docker_Directory" directory
ENV PYTHONPATH "${PYTHONPATH}:/Docker_Directory"

# Environment variables that will be used in the python application.
# To help to gather info for property works container.
ENV Path_Storage "/Docker_Directory/Storage"
ENV Name_File_Storage "User_Data.pkl"


# Create the Storage directory, where the data will be stored.
RUN mkdir -p /Docker_Directory/Storage

# Start application
CMD ["python", "./Main_Code/main.py"]