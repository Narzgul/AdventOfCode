visible_trees = []

with open("inputs/day8_input.txt") as puzzle_input:
    # Right to left
    for row, line in enumerate(puzzle_input):
        current_max = -1
        for column, char in enumerate(line.strip()):
            tree = int(char)
            if tree > current_max and [row, column] not in visible_trees:
                visible_trees.append([row, column])
                current_max = tree
    puzzle_input.seek(0)

    # Left to right
    for row, line in enumerate(puzzle_input):
        current_max = -1
        for column, char in reversed(list(enumerate(line.strip()))):
            tree = int(char)
            if tree > current_max:
                current_max = tree
                if [row, column] not in visible_trees:
                    visible_trees.append([row, column])
    puzzle_input.seek(0)

    # Top to bottom
    for column in range(len(puzzle_input.readline().strip())):
        puzzle_input.seek(0)
        current_max = -1
        for row in range(len(puzzle_input.readlines())):
            puzzle_input.seek(0)
            tree = int(puzzle_input.readlines()[row][column].strip())
            if tree > current_max:
                current_max = tree
                if [row, column] not in visible_trees:
                    visible_trees.append([row, column])
    puzzle_input.seek(0)

    # Top to bottom
    for column in range(len(puzzle_input.readline().strip())):
        puzzle_input.seek(0)
        current_max = -1
        for row in range(len(puzzle_input.readlines()) - 1, -1, -1):
            puzzle_input.seek(0)
            tree = int(puzzle_input.readlines()[row][column].strip())
            if tree > current_max:
                current_max = tree
                if [row, column] not in visible_trees:
                    visible_trees.append([row, column])

print(len(visible_trees))
