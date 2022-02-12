def binSearch(arr, match):
    activeArr = len(arr) - 1
    if arr[activeArr // 2] == match:
        print(match, "found at", activeArr // 2)
    else:
        activeArr = arr[0 : activeArr // 2]
        recurs = binSearch(activeArr, match)

    print(recurs)


binSearch([1, 55, 78, 90, 156, 1222, 6789], 91)
