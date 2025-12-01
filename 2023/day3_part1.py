import re

with open("inputs/day3_input.txt") as file:
    puzzle_input = file.readlines()

def is_symbol(char):
    if char in '#$%&*+-/=@':
        return True
    return False

sum_part_numbers = 0
for index in range(len(puzzle_input)):
    line = puzzle_input[index]
    numbers = re.finditer('[0-9]+', line)
    def in_bounds(index)
    for num in numbers:
        if ()
