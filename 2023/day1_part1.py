import re

with open("inputs/day1_input.txt") as file:
    puzzle_input = file.readlines()

total = 0

for line in puzzle_input:
    numbers = re.findall(pattern="[0-9]", string=line)
    first = numbers[0]
    last = numbers[-1]
    num_as_string = '' + first + last
    total += int(num_as_string)

print(total)
