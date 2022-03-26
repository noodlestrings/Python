def linSearch(arr, match):
    for index, value in enumerate(arr):
        if value == match:
            print(match, "found at", index)
