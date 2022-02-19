primArr = input("Enter a series of numbers to be sorted: ")
primArr = primArr.split()
for index, value in enumerate(primArr):
    primArr[index] = int(value)

#primArr = [5, 32, 2346, 346, 4, 3243, 3, 3, 223]
origPrimArr = primArr.copy()
sortedArr = ['placeholder']
sortedArr[0] = primArr[0]
primArr.pop(0)

for unsortedItem in primArr:
    if unsortedItem < sortedArr[0]:
        sortedArr.insert(0, unsortedItem)
    elif unsortedItem > sortedArr[len(sortedArr) - 1]:
        sortedArr.insert(len(sortedArr), unsortedItem)
    else:
        for sortedIndex in range(1, len(sortedArr)):
            if unsortedItem == sortedArr[sortedIndex]:
                sortedArr.insert(sortedIndex, unsortedItem)
                break
            if unsortedItem > sortedArr[sortedIndex - 1] and unsortedItem < sortedArr[sortedIndex]:
                sortedArr.insert(sortedIndex, unsortedItem)
                break


print(f"{origPrimArr} sorted to: \n{sortedArr}")
