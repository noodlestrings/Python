s = "y#fo##f"
t = "y#f#o##f"


sarr = []
tarr = []
for i in range(len(s)):
    sarr.append(s[i])
for j in range(len(t)):
    tarr.append(t[j])

while "#" in sarr:
    ind = sarr.index("#")
    sarr.pop(ind)
    if (ind - 1) >= 0:
        sarr.pop(ind - 1)  # index changes after list becomes shorter

while "#" in tarr:
    ind = tarr.index("#")
    tarr.pop(ind)
    if (ind - 1) >= 0:
        tarr.pop(ind - 1)

if tarr == sarr:
    print("true")
