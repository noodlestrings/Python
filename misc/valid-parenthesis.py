s = "(){"
arr = list(s)
invalid = True
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == "(" and arr[j] == ")":
            invalid = False
            break
        if arr[i] == "[" and arr[j] == "]":
            invalid = False
            break
        if arr[i] == "{" and arr[j] == "}":
            invalid = False
            break


print(invalid)
