strs = ["flowers", "flow", "flight"]
# firstWord = []
# common = []
# for letter in strs[0]:
#     firstWord.append(letter)
# for word in range(1, len(strs)):
#     for index, letter in enumerate(strs[word]):
#         if letter == firstWord[index]:
#             common.append(letter)
# print(common)
tempLetter = ""
tempLetter = strs[0][0]
for word in strs:
    for letter in range(1, len(word)):
        if word[letter - 1] in tempLetter:
            tempLetter += word[letter]
