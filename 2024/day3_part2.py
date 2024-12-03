import re

with open("inputs/day3_input.txt") as file:
    puzzle_input = file.readlines()

result = 0
do = True
o = re.escape("(")
c = re.escape(")")
re_ex = "(mul" + o + "[0-9]+,[0-9]+" + c + ")|(do" + o + c + ")|(don't" + o + c + ")"
for line in puzzle_input:
    mul_instructions = re.findall(re_ex, line)
    for inst in mul_instructions:
        if inst[0][:3] == "mul" and do:
            result += int(re.findall("[0-9]+", inst[0])[0]) * int(re.findall("[0-9]+", inst[0])[1])
        elif inst[2][:3] == "don":
            do = False
        elif inst[1][:2] == "do":
            do = True

print(result)