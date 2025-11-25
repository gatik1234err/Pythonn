class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def get_password(self):
        return self.__password


class Auth(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def login(self, username, password):
        return username == self.username and password == self.get_password()


print("Signup first:")
user_input = input("Enter username: ")
user_password = input("Enter password: ")


user = Auth(user_input, user_password)

print("\nLogin:")
login_username = input("Username: ")
login_password = input("Password: ")

if user.login(login_username, login_password):
    print("Login successful!")
else:
    print("Login failed!")
