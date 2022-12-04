with open("inputs/day1_input.txt") as file:
    puzzle_input = file.readlines()

largest = 0
current = 0

for line in puzzle_input:
    if len(line.strip()) != 0:
        current += int(line)
    else:
        if current > largest:
            largest = current
        current = 0

print(largest)