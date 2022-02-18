mydict = {"name": "sam", "age": 100, "city": "london"}
########################################################################
mydict2 = dict(name="Boris", age=50, city="london")
print(mydict2)
######################################################################
print(mydict2["name"])
############################################
mydict["age"] = 15
print(mydict)
#############################################
mydict["new-item"] = "new"
print(mydict)
#######################################################
del mydict["new-item"]  # or
mydict.pop("name")  # or
mydict.popitem()  # deletes last key and value
print(mydict)
#########################################################
mydict3 = {"a": 1, "b": 2, "c": 3, "d": 4}
if "b" in mydict3:
    print(mydict3["b"])
######################################################
try:
    print(mydict3["z"])
except:
    print("error")
##########################################################
for key, value in mydict3.items():  # .keys() returns keys; .values() returns the values for the keys
    print(key, "=", value)
###########################################################
mydict_copy = mydict3.copy()
#########################################################
mergedict1 = {"name": "john", "age": 199, "city": "Boston"}
mergedict2 = {"name": "mary", "age": 80, "email": "123@email.com"}

# all existing key values overwritten and extras appended
mergedict1.update(mergedict2)
print(mergedict1)
################################################################################
mytuple = (123, 456)
mytupledict = {(8, 7): "tuple", ("a", "b"): "tuple2", mytuple: "tuplevar"}
print(mytupledict)
##############################################################################