
import random

counter = 0
test = "ugay"
monkey1 = ""
monkey2 = ""
monkeyWords = []
dictionary = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " ", "."]


while True:
    random_number = random.randint(0, 53)
    monkey_letter = dictionary[random_number]
    print(monkey_letter)
    if counter >= 7:
        monkey2 += monkey_letter
        if test in monkey2:
            monkeyWords.append(test)
            print(monkeyWords)
            print("monkey2")
            exit()
    if len(monkey2) > 13:
        monkey2 = ""

    if len(monkey1) <= 14:
        monkey1 += monkey_letter
        if test in monkey1:
            monkeyWords.append(test)
            print(monkeyWords)
            print("monkey1")
            exit()
    if len(monkey1) > 13:
        monkey1 = ""
    counter += 1
