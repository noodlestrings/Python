mylist = list()  # creates empty list
mylist = []      # same ^
#########################################################
mylist2 = [1, 9, 3, 4, "among", 5, 6, 7]
print(mylist2[-1])  # last value
print(mylist2[-2])  # penultimate value
############################################################
if 25 in mylist2:
    print("present")
else:
    print("absent")
##############################################################
# value of pop can be stored, also if parameters of pop not empty
lastItemRemoved = mylist2.pop()
##############################################################
list2index = 0
mylist2.pop(list2index)  # pop removes using index
###############################################################
mylist2.remove("among")  # remove removes using value
################################################################
mylist2.reverse()
###############################################################
mylist2.clear()  # empties list
###############################################################
mylist2.sort()  # uses Tim sort, combo of merge and insertion, changes working list

# creates new list 'newlist' and assigns to sorted 'mylist2'
newlist = sorted(mylist2)
###############################################################

zeroList = [0] * 5   # creates new list with 5 zeroes
###############################################################

mylist3 = [1, 2, 3, 4, 5]
newlist3 = mylist2 + mylist3  # concatinating lists
##################################################################
print(newlist3[0:2])  # only prints up to second param
print(newlist3[:5])  # from beginning to index 5
print(newlist3[3:])  # from index 3 to end
print(newlist3[::2])  # goes from beginning to end, in increments of two
print(newlist3[::-1])  # reverses list
#################################################################
list_org = [1, 2, 3, 4, 5]
list_copy = list_org
list_copy.append(69)
print(list_org, list_copy)  # the change will be made on both lists

list_copy = list_org.copy()  # copys list, also copies by typecasting to list
