import uuid


class User:
    def __init__(self, name, age, class_section):
        self.id = uuid.uuid4()
        self.name = name
        self.age = age
        self.class_section = class_section


class Users:
    def __init__(self):
        self.users = []  # Initialize an empty list to store users

    def get_user(self, user_id):
        for user in self.users:
            if user_id == user.id:
                return user
        return False

    def add_user(self, user):
        self.users.append(user)

    def get_all_users(self):
        return self.users

    def delete_user(self, user_id):
        for index, user in enumerate(self.users):
            if user_id == user.id:
                print(f"User with {user.name} and {user.id} has been deleted")
                del self.users[index]
                return
        print(f"Unable to delete the user with {user_id}")



