# capitalise the first letter of each word in a string


def to_jaden_case(string):
    result = " ".join(elem.capitalize() for elem in string.split())
    return result


print(to_jaden_case("That is a real bruh meoment"))
