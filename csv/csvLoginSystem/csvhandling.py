import csv

from click import password_option


def remove_user_input_validation(username):
    passwordQuery = input(
        f"Please enter the password for account name {username}: ")
    UsrPswdExists = False
    with open(r'csv\csvLoginSystem\users.csv', 'r') as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        for line in csv_reader:
            if line['username'] == username and line['password'] == passwordQuery:
                UsrPswdExists = True
                break
    if UsrPswdExists != True:
        print("\nSorry, you entered the password and/or account name incorrectly")
        return "Invalid"

    # if exists:
    #     passwordQuery = input(f"Please enter the password for account name {username}: ")
    #     with open(r'csv\csvLoginSystem\users.csv', 'r+') as file:
    #         for line in csv_reader:
    #             if line[]


def check_user():
    with open(r'csv\csvLoginSystem\users.csv', 'r') as file:

        username = input("\nPlease enter your username: ")
        password = input("\nPlease enter your password: ")

        csv_reader = csv.DictReader(file, delimiter=";")
        usernameExists = False
        for line in csv_reader:
            if (line['username'] == username) and (line['password'] == password):
                usernameExists = True
                print("\nYou have successfully logged in to your account")
                exit()
            elif (line['username'] == username) and (line['password'] != password):
                usernameExists = True
                print("\nYou have entered the password incorrectly, please try again")
                check_user()

        if usernameExists == False:
            createAccount = input(
                "\nSorry, that account doesn't seem to exist.\nEnter 'a' to create a new account or 'r' to retry: ")
            if createAccount.lower() == 'a':
                add_user()
                exit()
            elif createAccount.lower() == 'r':
                check_user()


def add_user():
    with open(r'csv\csvLoginSystem\users.csv', 'r') as file:

        csv_reader = csv.DictReader(file, delimiter=";")

        firstName = input("\nEnter your first name: ")
        lastName = input("\nEnter your last name: ")
        userName = input("\nEnter your userName: ")
        email = input("\nEnter your email: ")
        password = input("\nEnter your password: ")

        for line in csv_reader:
            if line['username'] == userName:
                loginQuery = input(
                    f"\nAn account with the username {userName} already exists, enter 'L' to login or 'Q' to quit: ")
                if loginQuery.lower() == "l":
                    check_user()
                elif loginQuery.lower() == "q":
                    exit()

    fieldnames = ['first_name', 'last_name',
                  'username', 'email', 'password']

    with open(r'csv\csvLoginSystem\users.csv', 'a', newline="") as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
        csv_writer.writerow({'first_name': firstName, 'last_name': lastName,
                            'username': userName, 'email': email, 'password': password})
        print("\nAccount successfully created")


def remove_user():
    toBeDeleted = input(
        "\nPlease enter the username of the account to be removed: ")

    if remove_user_input_validation(toBeDeleted) == "Invalid":
        exit()

    csvContent = []
    with open(r'csv\csvLoginSystem\users.csv', 'r+') as file:
        csv_reader = csv.DictReader(file, delimiter=";")
        for line in csv_reader:
            if line['username'] != toBeDeleted:
                csvContent.append(line)

    with open(r'csv\csvLoginSystem\users.csv', 'w', newline="") as fileBackedUp:
        csv_writer = csv.DictWriter(fileBackedUp, fieldnames=['first_name', 'last_name',
                                                              'username', 'email', 'password'], delimiter=";")
        csv_writer.writeheader()
        for line in csvContent:
            csv_writer.writerow(line)

        print("\nDatabase updated")
