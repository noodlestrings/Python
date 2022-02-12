user_q = input("Please enter a string. Don't be sus... ")
user_q = list(user_q)
user_q.append("x")
print(user_q)

# among us


def among_us():
    for letter in range(0, len(user_q) + 1):
        print(letter)
        while letter != "x":
            if user_q[letter] == "a" or user_q[letter] == "A":
                if user_q[letter + 1] == "m":
                    if user_q[letter + 2] == "o":
                        if user_q[letter + 3] == "n":
                            if user_q[letter + 4] == "g":
                                if (
                                    user_q[letter + 5] == " "
                                    or user_q[letter + 5] == "u"
                                ):
                                    if user_q[letter + 6] == "s" or (
                                        user_q[letter + 6] == "u"
                                        and user_q[letter + 7 == "s"]
                                    ):
                                        print('"among us" detected. You were sus.')
                                        break


# amogus


# red

# sus

# imposter

# sussy


among_us()
