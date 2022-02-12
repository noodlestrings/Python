# number guessing game where computer guess a number between 1 and 20
# computer always wins
# first question: is your number odd or even
# second question: is your number more than or equal to 10 or is it less than 10
# third question: is your number a prime number? yes = guesses numbers
#                                                 no = is your number a multilpe of 3 (if odd)/ is your number a multiple of 4 (if even)
#                                                      guesses numbers

even_less_11_arr = ["2", "4", "6", "8", "10"]
even_more_10_arr = ["12", "14", "16", "18", "20"]
odd_less_11_arr = ["1", "3", "5", "7", "9"]
odd_more_10_arr = ["11", "13", "15", "17", "19"]

print(
    "Think of a number between '0' and '20' inclusive and I will try to guess your number."
)


odd_BOOL = False

quest_1 = input("Is your number odd or even? ")
if quest_1 == "odd":
    odd_BOOL = True


print("Interesting...")

less_than_11 = True

quest_2 = input("Is your number 'less' than 11, or 'more' than 10? ")
if quest_2 == "more":
    less_than_11 = False

print("I see...")

primenumber_BOOL = True
multiple_of_3_BOOL = False
multiple_of_4_BOOL = False

quest_3 = input("Is your number a prime number? ")
print("hmm...")
if quest_3 == "no":
    primenumber_BOOL = False
if odd_BOOL == True:
    multiple_of_3 = input("Is your number a multiple of 3? ")
    if multiple_of_3 == "yes":
        multiple_of_3_BOOL = True
elif odd_BOOL == False:
    multiple_of_4 = input("Is your number a multiple of 4? ")
    if multiple_of_4 == "yes":
        multiple_of_4_BOOL = True

print(
    odd_BOOL,
    less_than_11,
    primenumber_BOOL,
    multiple_of_3_BOOL,
    multiple_of_4_BOOL,
)
print("\n")

if odd_BOOL and less_than_11:
    print("odd and less than 11")
    if primenumber_BOOL:
        odd_less_11_arr.remove("9")
        # print("\n", odd_less_11_arr)
        if multiple_of_3_BOOL:
            print("Your number is 3")
        else:
            odd_less_11_arr.remove("3")
    else:
        print("Your number is 9")


elif odd_BOOL and less_than_11 == False:
    print("odd and more than 10")

elif odd_BOOL == False and less_than_11:
    print("even and less than 11")
elif odd_BOOL == False and less_than_11 == False:
    print("even and more than 10")

print(odd_less_11_arr)
if odd_BOOL and less_than_11:
    for number in range(0, len(odd_less_11_arr)):
        odd_and_less_final_guess = input(
            "Is " + str(odd_less_11_arr[number]) + " your number? "
        )
        if odd_and_less_final_guess == "yes":
            print("I knew it was " + str(odd_less_11_arr[number]))
            break
        # if odd_and_less_final_guess == "no":
        #   odd_less_11_arr.remove(odd_less_11_arr[number])
