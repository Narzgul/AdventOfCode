def find_score(x, y, peaks_to_ignore=None):
    if peaks_to_ignore is None:
        peaks_to_ignore = []
    score = 0
    if puzzle_input[y][x] == "9" and (x, y) not in peaks_to_ignore:
        print("Found at " + str(x) + ", " + str(y))
        peaks_to_ignore.append((x, y))
        return 1
    if x + 1 < len(puzzle_input[y]) and int(puzzle_input[y][x]) + 1 == int(puzzle_input[y][x + 1]):
        score += find_score(x + 1, y, peaks_to_ignore)  # Right
    if y + 1 < len(puzzle_input) and int(puzzle_input[y][x]) + 1 == int(puzzle_input[y + 1][x]):
        score += find_score(x, y + 1, peaks_to_ignore)  # Down
    if x - 1 >= 0 and int(puzzle_input[y][x]) + 1 == int(puzzle_input[y][x - 1]):
        score += find_score(x - 1, y, peaks_to_ignore)  # Left
    if y - 1 >= 0 and int(puzzle_input[y][x]) + 1 == int(puzzle_input[y - 1][x]):
        score += find_score(x, y - 1, peaks_to_ignore)  # Up
    return score


with open("inputs/day10_input.txt") as file:
    puzzle_input = file.readlines()
    for line in range(len(puzzle_input)): puzzle_input[line] = puzzle_input[line][:-1]

sum_score = 0
for y_pos in range(len(puzzle_input)):
    for x_pos in range(len(puzzle_input[y_pos])):
        if puzzle_input[y_pos][x_pos] == "0":
            sum_score += find_score(x_pos, y_pos)
            print(x_pos, y_pos, find_score(x_pos, y_pos))
print(sum_score)
