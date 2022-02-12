# You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

# Examples:
# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

# Concatenate the consecutive strings of strarr by 2, we get:

# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

# Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
# The first that came is "folingtrashy" so
# longest_consec(strarr, 2) should return "folingtrashy".

strarr = ["zone", "abigail", "theta", "form", "libe", "zas"]
k = -2


def longest_consec(strarr, k):
    array_length = len(strarr)
    longest_string = " "
    longest_str_k_is_1 = " "
    if k != 1:
        for i in range(0, array_length + 1):
            array_index_tmp = strarr[i : k + i : 1]
            # print(array_index_tmp)
            if array_index_tmp == strarr[array_length - 1 : array_length + k : 1]:
                break
            array_concat_tmp = array_index_tmp[0] + array_index_tmp[1]
            # print(array_concat_tmp)
            if len(array_concat_tmp) > len(longest_string):
                longest_string = array_concat_tmp
    elif k == 1:
        for x in strarr:
            if len(x) > len(longest_string):
                longest_string = x

    return longest_string


print(longest_consec(strarr, k))

# OFFICIAL SOLUTION:
# #def longest_consec(strarr, k):
#     result = ""

#     if k > 0 and len(strarr) >= k:
#         for index in range(len(strarr) - k + 1):
#             s = ''.join(strarr[index:index+k])
#             if len(s) > len(result):
#                 result = s

#     return result
