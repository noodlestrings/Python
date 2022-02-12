# prints the sum of the two smallest numbers in an array


def sum_two_smallest_numbers(numbers):
    sorted_array = sorted(numbers)
    return sorted_array[0] + sorted_array[1]


num_array = [7, 15, 12, 18, 22]
print(sum_two_smallest_numbers(num_array))
