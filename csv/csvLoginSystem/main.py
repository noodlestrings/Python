from csvhandling import check_user, add_user, remove_user

openingChoice = input(
    "Welcome to the CSV login system.\nTo log in to an account, press 'L'.\nTo add an account, press 'A'.\nTo remove an account, press 'R': ")


if openingChoice.lower() == 'l':  # login

    check_user()

elif openingChoice.lower() == 'a':  # add account
    add_user()
