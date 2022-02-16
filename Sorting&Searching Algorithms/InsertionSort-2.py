# DUPLICATE DATA WILL NOT RETURN DUPLICATED SORT
# print comments for debugging
primArr = [8, 3, 1, 5, 4, 97, 19, 1]
origPrimArr = str(primArr)
sortedArr = ['placeholder']
sortedArr[0] = primArr[0]
primArr.pop(0)


condition1 = False
incrementBool1 = False
i1 = 0
while condition1 == False:  # FOR INSERTING BEFORE FIRST VALUE
    #print(sortedArr, "sorted    ", primArr, "prim")
    #print(f"comparing {primArr[i1]}")
    if primArr[i1] < sortedArr[0]:
        #print(f"{primArr[i1]} < {sortedArr[0]}")
        sortedArr.insert(0, primArr[i1])
        primArr.pop(i1)
        #print(sortedArr, "sorted    ", primArr, "prim\n\n")
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

for primIndex, primValue in enumerate(primArr):
    #print(sortedArr, "sorted     ", primArr, "prim")
    for sortedIndex in range(1, len(sortedArr) - 1):
        # print(
        #    f"comparing {primValue} > {sortedArr[sortedIndex - 1]} \ncomparing {primValue} < {sortedArr[sortedIndex + 1]}\n")
        if primValue > sortedArr[sortedIndex - 1] and primValue < sortedArr[sortedIndex + 1]:
            sortedArr.insert(sortedIndex + 1, primValue)
            #print("inserted, next value is", primArr[primIndex + 1])
            break


print(f"{origPrimArr} sorted to: \n{sortedArr}")
