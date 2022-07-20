def bubblesort(arr):
    # INPUT SANITISATION
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
                print(arr1, "swap", swapCount)
        if swapsb == False:
            break

    print(f"\n\nArray sorted in {swapCount} swaps: ", arr1)


bubblesort(
    "123 5235 62348 3458 2389768 234958 183475 328 2849 5 328 59 12 5 837259 238 509 2431 5 371 28 5932 725 83215 7 238 1983 2 57283 59 258 2781 235"
)
# test nums: 123 5235 62348 3458 2389768 234958 183475 328 2849 5 328 59 12 5 837259 238 509 2431 5 371 28 5932 725 83215 7 238 1983 2 57283 59 258 2781 235
# 76547 3457 546 3456 3456345 4 456 73473 12325 432 754 4545534 4 4476 7 5 42357 5437 45 4 5374435 823490 3203 6784 03 306 -2345 6
# -234623543 2453 34764349430 393 6843 496 64 3 2 59 13825 27583 19 28 5783 921 822 57832 3920 54239 54945 595 9 5 2 3 4 5 6 0
