import re

with open("inputs/day3_input.txt") as file:
    puzzle_input = file.readlines()

result = 0
re_ex = "mul" + re.escape("(") + "[0-9]+,[0-9]+" + re.escape(")")
for line in puzzle_input:
    mul_instructions = re.findall(re_ex, line)
    for inst in mul_instructions:
        result += int(re.findall("[0-9]+", inst)[0]) * int(re.findall("[0-9]+", inst)[1])

print(result)