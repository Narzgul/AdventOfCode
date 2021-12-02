import re

with open("2021/inputs/day2_input.txt") as file:
    input = file.readlines()

horizontal_pos = 0
depht = 0
aim = 0
for line in input:
    if line.find("forward") == 0:
        horizontal_pos += int(re.findall("[0-9]", line)[0]) # Finds the number
        depht += aim * int(re.findall("[0-9]", line)[0]) # Finds the number
    elif line.find("down") == 0:
        aim += int(re.findall("[0-9]", line)[0]) # Finds the number
    else:
        aim -= int(re.findall("[0-9]", line)[0]) # Finds the number

print("Answer: " + str(horizontal_pos * depht))