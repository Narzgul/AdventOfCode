def find_score(x, y, ):
    score = 0
    if puzzle_input[y][x] == "9":
        print("Found at " + str(x) + ", " + str(y))
        return 1
    if x + 1 < len(puzzle_input[y]) and int(puzzle_input[y][x]) + 1 == int(puzzle_input[y][x + 1]):
        score += find_score(x + 1, y)  # Right
    if y + 1 < len(puzzle_input) and int(puzzle_input[y][x]) + 1 == int(puzzle_input[y + 1][x]):
        score += find_score(x, y + 1)  # Down
    if x - 1 >= 0 and int(puzzle_input[y][x]) + 1 == int(puzzle_input[y][x - 1]):
        score += find_score(x - 1, y)  # Left
    if y - 1 >= 0 and int(puzzle_input[y][x]) + 1 == int(puzzle_input[y - 1][x]):
        score += find_score(x, y - 1)  # Up
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
