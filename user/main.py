# from user import User, Users
# from prettytable import PrettyTable
#
# prettytable = PrettyTable()
# prettytable.add_column("ID", [])
# prettytable.add_column("Name", [])
# prettytable.add_column("Age", [])
# prettytable.add_column("Class", [])
#
# print("Welcome to the user section")
# print("Create User")
# users_object = Users()
# user_object = User("Rajeev", 29, "Mscit")
# users_object.add_user(user_object)  # Pass the user object to add_user() method
# users_object.add_user(user_object)  # Pass the user object to add_user() method
# all_users = users_object.get_all_users()
#
# for user in all_users:
#     prettytable.add_row([user.id, user.name, user.age, user.class_section])
# print(prettytable)


from user import User, Users  # Assuming you have a User and Users class defined in a user.py file
from prettytable import PrettyTable


def print_menu():
    print("User Operations Menu:")
    print("1. Add User")
    print("2. Save Users")
    print("3. Delete User")
    print("4. Show All Users")
    print("5. Exit")


def add_user(users_object, prettytable):
    name = input("Enter user's name: ")
    age = int(input("Enter user's age: "))
    class_section = input("Enter user's class: ")
    user_object = User(name, age, class_section)
    users_object.add_user(user_object)
    prettytable.add_row([user_object.id, user_object.name, user_object.age, user_object.class_section])
    print("User added successfully!")


def save_users(users_object):
    # Logic to save users (you can implement this based on your requirements)
    print("Users saved successfully!")


def get_all_users(users_object, prettytable):
    list_users = users_object.get_all_users()
    if list_users:
        print(prettytable)
    else:
        print("The list is empty")


def delete_user(users_object):
    user_id = input("Enter user ID to delete: ")
    user = users_object.get_user(user_id)
    if user:
        users_object.delete_user(user_id)
        print(f"User with ID {user_id} deleted successfully!")
    else:
        print(f"User with ID {user_id} not found!")


def set_table(prettytable):
    prettytable.field_names = ["ID", "Name", "Age", "Class"]


def main():
    print("Welcome to the User Operations Program")
    users_object = Users()
    prettytable = PrettyTable()
    set_table(prettytable)
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                add_user(users_object, prettytable)
            case "2":
                save_users(users_object)
            case "3":
                delete_user(users_object)
            case "4":
                get_all_users(users_object, prettytable)
            case "5":
                print("Exiting program...")
                return
            case default:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


