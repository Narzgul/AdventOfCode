visible_trees = []

with open("inputs/day8_input.txt") as puzzle_input:
    for row, line in enumerate(puzzle_input):
        current_score = 1
        for column, char in enumerate(line.strip()):
            puzzle_input.seek(0)
            tree = int(char)
            i = 1
            while int(puzzle_input.readlines()[row + i][column]) < tree:
                i += 1
            current_score *= i

print(len(visible_trees))
