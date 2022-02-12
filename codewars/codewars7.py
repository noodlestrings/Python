# finds the odd number out in an array
def find_uniq(arr):
    if arr[0] != arr[1]:
        if arr[0] != arr[2]:
            return arr[0]
        else:
            return arr[1]
    else:
        for i in arr[2:]:
            if i != arr[0]:
                return i


array = [
    2,
    4,
    4,
    4,
    4,
    4,
]
print(find_uniq(array))
