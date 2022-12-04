with open("inputs/day3_input.txt") as file:
    puzzle_input = file.readlines()


def get_priority(c):
    if ord(c) > 96:
        return ord(c) - 96
    else:
        return ord(c) - 38


priorities_sum = 0

for i in range(0, len(puzzle_input), 3):
    line1, line2, line3 = puzzle_input[i].strip(), puzzle_input[i + 1].strip(), puzzle_input[i + 2].strip()
    for char in line1:
        if line2.find(char) != -1 and line3.find(char) != -1:
            priorities_sum += get_priority(char)
            break

print(priorities_sum)
