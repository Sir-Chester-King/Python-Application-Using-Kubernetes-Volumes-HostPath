# Import modules section.
from clean_console import *
from create_data import create_user
from modify_data import *
from view_data import *


def main():
    menu_app = {
        "1": "Create new user",
        "2": "View list all users",
        "3": "Modify existing user"
    }
    options_available = list(menu_app.keys())

    # Print the menu app as readable for users.
    print("{:<10} {:<15}".format('Option', 'Action'))
    for key, value in menu_app.items():
        print("{:<10} {:<15}".format(key, value))
    print("Please, insert only the available value from the menu.")

    # Loop state in case of wrong input option insert
    option_chosen = str(input("Insert option: "))
    while option_chosen not in options_available:
        option_chosen = str(input("Insert option: "))

    # Call the property function based on the user's chosen option.
    match option_chosen:
        case "1":
            # Loop if the user wants to create a multiple "User Objects"
            loop_users = True

            while loop_users:
                # Clear the console.
                clear()
                create_user()

                while True:
                    print("Do you want to create another User?")
                    choose = input("Yes or No (y / n): ").lower()
                    if choose == "y":
                        break
                    if choose == "n":
                        loop_users = False
                        break
        case "2":
            # Clear the console.
            clear()
            list_all_users()
        case "3":
            # Clear the console.
            clear()
            modify_user()
        case _:
            return 0


# __name__ is a special built-in variable that exists in every module (a module is simply a Python file).
# __main__ is a string that Python assigns to the __name__ variable when the module is executed as the main program.
# It serves as an entry point for the script execution.
# The if __name__ == "__main__": condition checks whether the script is being run directly or being imported.
# Code inside this if block will only execute if the script is run directly not when it is imported.
if __name__ == "__main__":
    main()
