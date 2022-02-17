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
