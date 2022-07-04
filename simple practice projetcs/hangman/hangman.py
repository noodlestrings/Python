import random
import time

with open(
    r"C:\Users\Sam\Documents\Programming\Python GIT REPO\simple practice projetcs\hangman\words.txt",
    "r+",
) as word_file:
    rand_num = random.randint(0, 100)
    lines = word_file.readlines()
    random_word = lines[rand_num]
    random_word = list(random_word)
    random_word.pop()
    # print(random_word)

print("\nYour guesses will be counted - duplicate guesses will not be added to total number of guesses")
print("\t\t\t     - multiple instances of the same letter will be automatically added and will only count for 1 guess")
begin_input = input("\n\nPress 'S' to start the game: ")
if begin_input == "S" or "s":
    print("The word is", len(random_word), "characters long.")
    # print("THE WORD IS", random_word)

usr_word = [" "] * len(random_word)
# print(usr_word)
# print(random_word)

entered_letters = [" "]
add_to_entered_letters = True

while_control = 0
guessnum = 0
while while_control != len(random_word):
    usr_guess = input("Enter a letter: ")
    add_to_entered_letters = True
    for enteredletter in entered_letters:
        if usr_guess == enteredletter or len(usr_guess) > 1:
            add_to_entered_letters = False
    if add_to_entered_letters == True:
        entered_letters.append(usr_guess)
    # print("ENTERED:", entered_letters)
    if add_to_entered_letters == True:
        for index, letter in enumerate(random_word):
            if usr_guess == letter:
                usr_word[index] = random_word[index]
                while_control += 1
        guessnum += 1

    print(usr_word)
    # print(while_control)
    print(guessnum, "guesses")


def arrtostr(random_word):
    new = ""
    for i in random_word:
        new += i

    return new


arrtostr_res = arrtostr(random_word)
print(
    "Congratulations, you guessed " + "\"" + arrtostr_res + "\"" + " in",
    guessnum,
    "guesses.",
)
