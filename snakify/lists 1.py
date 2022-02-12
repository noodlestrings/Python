lst = ["4", " ", "5", " ", "3", " ", "4", " ", "2", " ", "3"]  # to be added as input
resolute = []
for item in lst:
    if item != " ":
        item = int(item)
        resolute.append(item)
# print(resolute)

for index in range(0, len(resolute)):
    if index % 2 == 0 or index == 0:
        print(resolute[index])
