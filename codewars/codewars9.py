# given a string of letters, print the string as such:
# ("abcd") -> "A-Bb-Ccc-Dddd"
# ("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
def accum(s):
    return "-".join(c.upper() + c.lower() * i for i, c in enumerate(s))


print(accum("aabgdsf"))
