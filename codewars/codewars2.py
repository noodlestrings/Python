# calculates how many vowels are in a string


def get_count(input_str):
    num_vowels = 0
    for letter in input_str:
        if (
            letter == "a"
            or letter == "e"
            or letter == "i"
            or letter == "o"
            or letter == "u"
        ):
            num_vowels += 1

    return num_vowels


get_count("there are 4")
