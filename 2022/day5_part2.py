import re

with open("inputs/day5_input.txt") as puzzle_input:
    max_height = 0
    stacks = []

    # Get number of stacks and create them
    for max_height, line in enumerate(puzzle_input):
        if line.strip()[-1].isdigit():
            for i in range(int(line.strip()[-1])):
                stacks.append([])  # Create as many stacks as necessary
            break

    puzzle_input.seek(0)  # Reset position in file to top

    # Read starting state of stacks
    for i in range(max_height):
        line = puzzle_input.readline()
        for j in range(1, len(line), 4):
            if line[j].isalpha():  # Is letter
                stacks[(j - 1) // 4].insert(0, line[j])  # Insert to bottom

    puzzle_input.readline()  # Skip label line
    puzzle_input.readline()  # Skip empty line

    for line in puzzle_input:
        str_numbers = re.findall("[0-9]+", line)
        numbers = list(map(int, str_numbers))  # Convert to int list
        pop_index = len(stacks[numbers[1] - 1]) - numbers[0]
        for i in range(numbers[0]):
            stacks[numbers[2] - 1].append(stacks[numbers[1] - 1].pop(pop_index))

    for stack in stacks:
        print(stack.pop(), end="")  # Print top elements
