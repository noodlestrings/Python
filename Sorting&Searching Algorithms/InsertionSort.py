# DUPLICATE DATA WILL BE INSERTED ADJACENT
# CREATE FUNCTIONS FOR EACH PART OF SORT

primArr = input("Enter a series of numbers to be sorted: ")
primArr = primArr.split()
for index, value in enumerate(primArr):
    primArr[index] = int(value)

#primArr = [1, 6, 48, 3, 2, 9, 6, 43]
origPrimArr = primArr.copy()
sortedArr = ['placeholder']
sortedArr[0] = primArr[0]
primArr.pop(0)


condition1 = False
incrementBool1 = False
i1 = 0
while condition1 == False:  # FOR INSERTING BEFORE FIRST VALUE
    if primArr[i1] < sortedArr[0]:
        sortedArr.insert(0, primArr[i1])
        primArr.pop(i1)
    else:
        incrementBool1 = True
    if i1 == len(primArr) - 1:
        condition1 = True

    if incrementBool1:
        i1 += 1


condition2 = False
incrementBool2 = False
i2 = 0
while condition2 == False:  # FOR INSERTING AFTER LAST VALUE
    if primArr[i2] > sortedArr[len(sortedArr) - 1]:
        sortedArr.insert((len(sortedArr)), primArr[i2])
        primArr.pop(i2)
    else:
        incrementBool2 = True

    if i2 == len(primArr) - 1:
        condition2 = True
    if incrementBool2:
        i2 += 1

for primValue in primArr:
    for sortedIndex in range(1, len(sortedArr)):
        #zlower = sortedArr[sortedIndex - 1]
        #zupper = sortedArr[sortedIndex]
        if primValue == sortedArr[sortedIndex]:
            sortedArr.insert(sortedIndex, primValue)
            break
        if primValue > sortedArr[sortedIndex - 1] and primValue < sortedArr[sortedIndex]:
            sortedArr.insert(sortedIndex, primValue)
            break


print(f"{origPrimArr} sorted to: \n{sortedArr}")
