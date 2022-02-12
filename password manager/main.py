from cryptography.fernet import Fernet

master_pwd = input("Enter the master password: ")

mode = input(
    'Type "enter" to enter a new password, "view" to view saved passwords, or "q" to quit: '
).lower()


def enter():
    name = input("Enter the account name: ")
    pwd = input("Enter the password: ")
    with open(r"C:\Users\Sam\Documents\Python\password manager\pswd.txt", "a") as file:
        file.write(
            name + " " + pwd + "\n"
        )  # need to use .write for file as its an object not a string (that would take .append)


def view():
    with open(
        r"C:\Users\Sam\Documents\Python\password manager\pswd.txt", "r+"
    ) as file:  # r converts a normal string into a raw string to be used as a file path
        for line in file:
            data = line.rstrip()  # removes white space
            usrname, pswd = data.split(" ")
            print("username =", usrname, "~ password =", pswd)


if mode == "q":
    exit()
if mode == "enter":
    enter()
elif mode == "view":
    view()
else:
    print("Invalid mode")

# https://youtu.be/DLn3jOsNRVE?t=5359
