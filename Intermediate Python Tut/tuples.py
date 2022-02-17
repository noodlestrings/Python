# Tuple: immutable, allows for duplicates, for grouping similar data to one variable

mytuple = ("sam", 100, "London")   # also works without brackets
###################################################################################################
# MUST have comma after one value in tuple to be a tuple, otherwise saved as str/int/bool etc
mytuple1 = ("python",)
print(type(mytuple1))
#############################################################################################
mytuple3 = tuple(["sam", 100, "london"])  # can cast lists to tuples
###########################################################################################
print(mytuple3[0])    # access items in tuple as with lists
####################################################################
# mytuple[3] = "john"  # = TypeError     # tuples are immutable
############################################################################
for i in mytuple3:
    print(i)                 # tuples are iterable
######################################################################
if "sam" in mytuple3:
    print("present")
else:
    print("no")
######################################################
print(mytuple3.count("sam"))
print(mytuple3.index("sam"))  # returns first index of occurence of param
################################################
name, age, city = mytuple3  # assignment must account for all elements in tuple
print(name)
print(age)
print(city)
####################################################################
mytuple4 = (0, 1, 2, 3, 4)
i1, *i2, i3 = mytuple4
print(i1)  # first item
print(i3)  # last item
print(i2)  # everything between start and end casted to list
######################################################################
