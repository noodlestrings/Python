def bubblesort(arr1):
    # arr1 = arr.split()  # allows for multiple digit nums

    # # split casts values to strs
    # for index, value in enumerate(arr1):
    #     arr1[index] = int(value)

    swapCount = 0
    swapsb = True
    while swapsb:
        swapsb = False
        for item in range(len(arr1) - 1):
            swapBack = 0
            swapForward = 0
            if arr1[item] > arr1[item + 1]:
                swapBack = arr1[item + 1]
                swapForward = arr1[item]
                arr1[item] = swapBack
                arr1[item + 1] = swapForward
                swapsb = True
                swapCount += 1
                #print(arr1, "swap", swapCount)
        if swapsb == False:
            break

    #print(f"\n\nArray sorted in {swapCount} swaps: ", arr1)
    return arr1


#bubblesort("312 5436 4 3 464 3 4 6 7 8 65 68 5 343 2 35 643 778 865")
bubblesort([312, 4, 5436, 3, 464, 3, 4, 6, 7, 8, 65, 68, 5, 343, 2, 35, 643, 778, 865])