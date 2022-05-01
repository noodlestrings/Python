s = "ab#c"
t = "ad#c"

sarr = []
tarr = []
for i in range(len(s)):
    sarr.append(s[i])
for j in range(len(t)):
    tarr.append(s[j])

while "#" in sarr:
    ind = sarr.index("#")
    sarr.pop(ind - 1)
    sarr.pop(ind - 1) #index changes after list becomes shorter

while "#" in tarr:
    ind = tarr.index("#")
    tarr.pop(ind - 1)
    tarr.pop(ind - 1)

if tarr == sarr :
    return true
