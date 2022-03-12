# sets: unordered, mutable, no duplicates
myset = {1, 2, 3, 1, 2}
print(myset)
set2 = set("Hello")  # arbitrary order
print(set2)

set3 = set()  # to make an empty set
set3.add(1)
set3.add(3)
set3.add(2)
set3.add(4)
set3.add(5)
set3.remove(4)
set3.discard(5)  # removes element: if not found, no key error flagged
print(set3)
############################################
for value in set2:
    print(value)
#################################################
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)  # combines sets into new set u without duplication
i = odds.intersection(primes)  # finds common values from both sets
print(i)
####################################################
seta = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setb = {1, 5, 6, 7, 15}
setc = {3, 2, 6, 4, 88}
set0 = {1, 2, 3, 4, 5}
set01 = {5, 6, 7, 8, 9}
set02 = {3, 6, 8, 5, 2, 1}
diff = seta.difference(setb)  # returns all elements of seta not in setb
print(diff)

# returns all elements of seta and setb but not elements in both sets
symdiff = seta.symmetric_difference(setb)
print(symdiff)

seta.update(setb)
print(seta)  # adds all elements from another set without dups

seta.intersection_update(setc)  # keeps only elements from both sets
print("\n\n", seta)

set0.difference_update(set01)  # removes element found in another set
print(set0)

# only keeps elements found in both sets, but not elements that are found in both
set02.symmetric_difference_update(set0)
print(set02)
####################################################################################
set001 = {1, 2, 3, 4}
set002 = {1, 2}
setyes = {1, 2, 3}
setno = {4, 5, 6}
print("\n\n")
print(set002.issubset(set001))
print(set001.issuperset(set002))  # does first set contain all elements of 2nd
print(setyes.isdisjoint(setno))  # do none of the values match
###########################################################################################
# frozen set is immutable set
a = frozenset([1, 2, 3, 4, 5])
print(a)
