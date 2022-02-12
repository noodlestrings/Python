def factorial(usr):
    if usr < 0:
        return -1
    elif usr < 2:
        return 1
    else:
        return usr * factorial(usr - 1)


usr = int(input("Enter a number to find its factorial: "))
5
while usr != 1.1:
    print(factorial(usr))
    usr = int(input("Enter a number to find its factorial: "))
# this is for git testing purposes
# test for vscode source control panel
