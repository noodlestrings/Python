# gives the postition in the alphabet of each letter in a string

from itertools import count
from string import ascii_lowercase


def alphabet_position(text):
    letter_mapping = dict(zip(ascii_lowercase, count(1)))
    indexes = [
        letter_mapping[letter] for letter in text.lower() if letter in letter_mapping
    ]

    return " ".join(str(index) for index in indexes)


alphabet_position("The sunset sets at twelve o' clock.")
