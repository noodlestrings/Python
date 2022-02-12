# goes through each item in an array to check if they are true or false: true meaning there is a sheep present


def count_sheeps(sheep):
    TrueCounter = 0
    FalseCounter = 0
    for instance in sheep[::1]:
        if instance == True:
            TrueCounter += 1
    return TrueCounter


array1 = [
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    True,
    False,
    True,
    False,
    True,
    False,
    False,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    True,
    True,
]

print(count_sheeps(array1))
