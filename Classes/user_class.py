# Class for the User objects instances.
# The purpose of the class is to set and get user's personal info.
class User(object):

    # Declare the constructor function.
    # It's the initialize function called when a new object instance in created
    def __init__(self, name, surname, address, phone_number):
        # Here declared the attributes of the instances
        # The keyword "self" indicate the object instance, the other are the parameters send via function "constructor"
        self.name = name
        self.surname = surname
        self.address = address
        self.phone_number = phone_number

    # SET Functions ------------- #
    def set_name(self, name):
        self.name = str(name)

    def set_surname(self, surname):
        self.surname = str(surname)

    def set_address(self, address):
        self.address = str(address)

    def set_phone_number(self, phone_number):
        self.phone_number = str(phone_number)

    # GET Functions ------------- #
    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_address(self):
        return self.address

    def get_phone_number(self):
        return self.phone_number
