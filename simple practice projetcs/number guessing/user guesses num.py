### REWRITE!!!
import random
import time

congrat_message = "Congratulations! That was the correct number! \n"
fail_message = "Unlucky! That was not the correct number! \n"
input_message = "Enter a number between '0' and '20': "
print(
    "I will think of a number between '1' and '20' inclusive. I will give you hints and you have to try and guess what number I am thinking of: "
)

random_number = random.randint(0, 20)


def even_or_odd():
    returnvalue = ""
    if random_number % 2 == 0:
        returnvalue = "The number is even. "
    else:
        returnvalue = "The number is odd. "
    return returnvalue


def prime_number():
    is_prime = "The number is a prime number. "
    not_prime = "The number is not a prime number. "
    flag = False
    if random_number > 1:
        for i in range(2, random_number):
            if (random_number % i) == 0:
                flag = True
                break
    if flag or random_number == 1:
        return not_prime
    else:
        return is_prime


def less_than_ten():
    less_equal_10 = "The number is less than or equal to 10. "
    if random_number > 10:
        less_equal_10 = "The number is more than 10. "
    return less_equal_10


# print(random_number)

# HINT 1
print(even_or_odd())
hint_1 = int(input(input_message))
if hint_1 == random_number:
    print(congrat_message)
    time.sleep(4.5)
    exit()
else:
    print(fail_message)


# HINT 2
print(prime_number())
hint_2 = int(input(input_message))
if hint_2 == random_number:
    print(congrat_message)
    time.sleep(4.5)
    exit()
else:
    print(fail_message)

# HINT 3
print(less_than_ten())
hint_3 = int(input(input_message))
if hint_3 == random_number:
    print(congrat_message)
    time.sleep(4.5)
    exit()
else:
    print(fail_message)


### ORIGINGAL!!!


# number guessing game in which program picks a number between 1 and 20. The user has 4 chances to enter the correct number.
# there is an initial hint - is the number odd or even
# there is a second hint - is the number less than or equal to 10
# there is a third hint - is the number a prime number


# import random

# congrat_message = "Congratulations! That was the correct number! \n"
# fail_message = "Unlucky! That was not the correct number! \n"

# random_number = random.randint(0, 20)
# # print(random_number)   #to know what the random number is

# # function to check prime number
# def prime_number(random_number):
#     random_number = random_number
#     flag = False
#     if random_number > 1:
#         for i in range(2, random_number):
#             if (random_number % i) == 0:
#                 flag = True
#                 break
#     if flag:
#         return "The number is not a prime number"
#     else:
#         return "The number is a prime number"


# # function to check prime number

# # function to check even or odd
# def even_or_odd():
#     returnvalue = ""
#     if random_number % 2 == 0:
#         returnvalue = "even"
#     else:
#         returnvalue = "odd"
# 	return returnvalue

# # function to check >= 10


# # HINT 1: EVEN ROUTE
# if even_or_odd() == "even":
#     hint_1_even_input = int(
#         input("The number is even. Enter a guess between '0' and '20': ")
#     )
#     if hint_1_even_input == random_number:
#         print(congrat_message)
#     elif hint_1_even_input != random_number:
#         print(fail_message)
#     elif even_or_odd() == "odd":

# # HINT 1


#         # HINT 2
#         if random_number <= 10:
#             hint_2_even_input_less_10 = int(
#                 input(
#                     "The number is less than or equal to 10. Enter your second guess between '0' and '20': "
#                 )
#             )

#             if hint_2_even_input_less_10 == random_number:
#                 print(congrat_message)
#             elif hint_2_even_input_less_10 != random_number:
#                 print(fail_message)
#                 # HINT 2

#                 # HINT 3
#                 hint_3_prime = int(
#                     input(
#                         (prime_number(random_number))
#                         + ". Enter your second guess between '0' and '20':  "
#                     )
#                 )
#                 if hint_3_prime == random_number:
#                     print(congrat_message)
#                 elif hint_3_prime != random_number:
#                     print(
#                         fail_message, "The number I was thinking of was", random_number
#                     )
#         # HINT 3

#         # HINT 2
#         elif random_number > 10:
#             hint_2_even_input_more_10 = int(
#                 input(
#                     "The number is more than 10. Enter your second guess between '0' and '20': "
#                 )
#             )
#             if hint_2_even_input_more_10 == random_number:
#                 print(congrat_message)
#             elif hint_2_even_input_more_10 != random_number:
#                 print(fail_message)
#             # HINT 2

#             # HINT 3
#             hint_3_prime = int(
#                 input(
#                     (prime_number(random_number))
#                     + ". Enter your second guess between '0' and '20':  "
#                 )
#             )
#             if hint_3_prime == random_number:
#                 print(congrat_message)
#             elif hint_3_prime != random_number:
#                 print(fail_message, ". The number I was thinking of was", random_number)
# # HINT 3


# HINT 1: ODD ROUTE
# elif random_number % 2 != 0:
#     hint_1_odd_input = int(
#         input("The number is odd. Enter a guess between '0' and '20': ")
#     )
#     if hint_1_odd_input == random_number:
#         print(congrat_message)
#     elif hint_1_odd_input != random_number:
#         print(fail_message)

#         if random_number <= 10:
#             hint_2_odd_input_less_10 = int(
#                 input(
#                     "The number is less than or equal to 10. Enter your second guess between '0' and '20': "
#                 )
#             )

#             if hint_2_odd_input_less_10 == random_number:
#                 print(congrat_message)
#             elif hint_2_odd_input_less_10 != random_number:
#                 print(fail_message)

#             hint_3_prime_odd = int(
#                 input(
#                     (prime_number(random_number))
#                     + ". Enter your second guess between '0' and '20':  "
#                 )
#             )
#             if hint_3_prime_odd == random_number:
#                 print(congrat_message)
#             elif hint_3_prime_odd != random_number:
#                 print(fail_message, "The number I was thinking of was", random_number)

#         elif random_number > 10:
#             hint_2_odd_input_more_10 = int(
#                 input(
#                     "The number is more than 10. Enter your second guess between '0' and '20': "
#                 )
#             )

#             if hint_2_odd_input_more_10 == random_number:
#                 print(congrat_message)
#             elif hint_2_odd_input_more_10 != random_number:
#                 print(fail_message)

#             hint_3_prime_odd = int(
#                 input(
#                     (prime_number(random_number))
#                     + ". Enter your second guess between '0' and '20':  "
#                 )
#             )
#             if hint_3_prime_odd == random_number:
#                 print(congrat_message)
#             elif hint_3_prime_odd != random_number:
#                 print(fail_message, ". The number I was thinking of was", random_number)
