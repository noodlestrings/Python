primArr = [5, 4, 3, 6, 1, 8, 9, 7]
sortedArr = ['placeholder']
sortedArr[0] = primArr[0]  #sets first value of primary array to sorted array
primArr.pop(0)             #removes this from primary array

def placeInSortedArr(value):   #essentially a bubble sort
    for sortedIndex, sortedItem in enumerate(sortedArr):
        if value < sortedItem and sortedIndex == 0:    #list index out of range error FIXX
            sortedArr.insert(0, value)
            
        elif value < sortedArr[sortedIndex + 1] and value > sortedArr[sortedIndex - 1] and sortedIndex != 0:
            print("sus")


for value in primArr:
    if value > sortedArr[(len(sortedArr) - 1)]:
        sortedArr.append(value)
    elif value < sortedArr[(len(sortedArr) - 1)]:
        for index, s in enumerate(sortedArr):
            if value < s and len(sortedArr) == 1:
                print("first if")
                sortedArr.insert(0, value)        #steps after iterate through sorted to determine where to insert value, where length of sorted array is not > 1, inserted before first value
            elif value < s and len(sortedArr) > 1:
                print("second elif")
                placeInSortedArr(value)
                #oneLeftIterator = 1   #~~~~~~~~~~~~~~~~~~~~~ MAKE FUNCTION FOR BELOW 
                #oneLeft = sortedArr[index - oneLeftIterator]
                #while value < oneLeft:
                #    print(oneLeft)
                #    oneLeftIterator += 1
                #sortedArr.insert((index - oneLeftIterator), value)    
                    
            
print(sortedArr)




