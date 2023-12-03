import re

with open("inputs/day1_input.txt") as file:
    puzzle_input = file.readlines()

total = 0
number_strings = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

for line in puzzle_input:
    first_index = -1
    first_string_value = -1
    for string in number_strings.keys():
        index = line.find(string)
        if index != -1 and (index < first_index or first_index == -1):
            first_index = index
            first_string_value = number_strings[string]

    for integer in range(1, 10):
        index = line.find(str(integer))
        if index != -1 and (index < first_index or first_index == -1):
            first_index = index
            first_string_value = integer

    last_index = -1
    last_string_value = -1
    for string in number_strings.keys():
        index = line.rfind(string)
        if index > last_index or last_index == -1:
            last_index = index
            last_string_value = number_strings[string]

    for integer in range(1, 10):
        index = line.rfind(str(integer))
        if index > last_index or last_index == -1:
            last_index = index
            last_string_value = integer

    num_as_string = '' + str(first_string_value) + str(last_string_value)
    print(num_as_string)
    total += int(num_as_string)

print(total)
