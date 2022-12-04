with open("inputs/day3_input.txt") as file:
    puzzle_input = file.readlines()


def get_priority(c):
    if ord(c) > 96:
        return ord(c) - 96
    else:
        return ord(c) - 38


priorities_sum = 0

for line in puzzle_input:
    compartment1 = line[:len(line) // 2]  # From start to mid
    compartment2 = line[len(line) // 2:].strip()  # From mid to end
    for char in compartment1:
        if compartment2.find(char) != -1:
            priorities_sum += get_priority(char)
        break

print(priorities_sum)
