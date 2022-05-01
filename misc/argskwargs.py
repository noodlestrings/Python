def function(*nums):
    for number in nums:
        print(number)


function(1, 2, 3, 2, 2, 5, 3, 2)


def function(**employees):
    for key, value in employees.items():
        print(key, value)


function(name="sam", age=15, location="london")
