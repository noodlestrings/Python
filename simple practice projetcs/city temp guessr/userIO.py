import random
from api import get_city_temp
from cities import cities

running = True
while running:
    randomIndex = random.randint(0, len(cities) - 1)
    usrChoice = input("Press q to quit or enter to continue: ")
    if usrChoice.lower() == "q":
        running = False
        break

    print("\n\nYou will have 3 guesses to guess the temperature of the given city within 5 degrees Celsius.")

    city = cities[randomIndex]
    if "+" in city:
        city = city.replace("+", " ")

    temp = get_city_temp(cities[randomIndex])

    guessNo = 3
    while guessNo > 0:
        print(f"\nYou have {guessNo} guesses remaining.")
        guessTemp = int(input(f"Guess the temperature in {city}: "))
        print("\n")
        if (guessTemp > temp - 5) and (guessTemp < temp + 5):
            print(
                f"Congratulations! You correctly guessed the temperature in {city} to be close to {temp} degrees")
            break
        guessNo -= 1
        if guessNo == 0:
            print(
                f"Sorry, you didn't get the temperature in {city}, it was actually {temp} degrees there.")
