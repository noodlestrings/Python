triple = """This is used for mutliline strings\
and documentation"""
# \ makes print of a multiline string not mutline at execution


string = "Lorem impsum whatever else comes after this         "
# index 5 not included; value after second colon controls steps
substring = string[:5:2]
print(substring)

if "L" in string:
    print("Present")

strippedString = string.strip()
print(strippedString)  # removes whitespace

print(string.startswith("Lorem"))
print(string.startswith("L"))
print(string.endswith("x"))

# finds index of first occurence, can use sequences of letters as param
print(string.find('a'))
print(string.count("e"))
print(string.replace("else", "reaplcament"))

lst = string.split()
# splits each word into element in list, defualt argument is ' '
lst = string.split("e")
print(lst)
# concatinates all values of list; space in "" joins wihth space
newstr = "".join(lst)
print(newstr)
#############################################################################
var = "strubg"
num = 2
stringPerc = "the variable is %s" % var  # same as C formatting: %f, %.2f etc
stringForm = "the variable is {} and {}".format(
    var, num)  # {:.2f} prints 2 decimal places
