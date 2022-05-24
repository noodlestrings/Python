from csvhandling import check_user, add_user, remove_user


validChoice = False
while validChoice == False:

    openingChoice = input(
        "Welcome to the CSV login system.\n\nTo log in to an account, press 'L'.\nTo add an account, press 'A'.\nTo remove an account, press 'R': ")

    if openingChoice.lower() == 'l':  # login
        check_user()
        validChoice = True

    elif openingChoice.lower() == 'a':  # add account
        add_user()
        validChoice = True

    elif openingChoice.lower() == 'r':  # remove
        remove_user()
        validChoice = True

    else:
        print("Sorry, that was not an option available. Please try again.\n\n")
