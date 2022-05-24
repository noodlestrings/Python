import csv


def check_user():
    with open(r'csv\csvLoginSystem\users.csv', 'r') as file:

        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        csv_reader = csv.DictReader(file, delimiter=";")
        for line in csv_reader:
            if (line['username'] == username) and (line['password'] == password):
                print("You have successfully logged in to your account")
                exit()
            elif (line['username'] == username) and (line['password'] != password):
                print("You have entered the password incorrectly, please try again")
                check_user()
            else:
                createAccount = input(
                    "Sorry, that account doesn't seem to exist.\nEnter 'a' to create a new account or 'r' to retry: ")
                if createAccount.lower() == 'a':
                    add_user()
                elif createAccount.lower() == 'r':
                    check_user()


def add_user():
    with open(r'csv\csvLoginSystem\users.csv', 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        firstName = input("Enter your first name: ")
        lastName = input("Enter your last name: ")
        userName = input("Enter your userName: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        for line in csv_reader:
            if line['username'] == userName:
                loginQuery = input(
                    f"An account with the username {userName} already exists, enter 'L' to login or 'Q' to quit: ")
                if loginQuery.lower() == "l":
                    check_user()
    fieldnames = ['first_name', 'last_name',
                  'username', 'email', 'password']
    with open(r'csv\csvLoginSystem\users.csv', 'a', newline="") as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
        csv_writer.writerow({'first_name': firstName, 'last_name': lastName,
                            'username': userName, 'email': email, 'password': password})


def remove_user():
    pass


# "check_user("Jdoe69", "johndoe123")

# with open(r'csv\csvLoginSystem\users.csv', 'r') as file:
#     csv_reader = csv.DictReader(file, delimiter=';')
#     for line in csv_reader:
#         print(line['first_name'])
