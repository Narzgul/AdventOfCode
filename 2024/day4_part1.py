with open("inputs/day4_input.txt") as file:
    puzzle_input = file.readlines()

def find_occurrences(x, y):
    occurrences = 0
    xmas = "XMAS"
    # Right
    for i in range(len(xmas)):
        if (x+i) >= len(puzzle_input[y]): break
        if puzzle_input[y][x+i] == xmas[i]: occurrences += 0.25
    if occurrences % 1 != 0: occurrences -= occurrences % 1
    # Down Right
    for i in range(len(xmas)):
        if (x+i) >= len(puzzle_input[y]) or (y+i) >= len(puzzle_input): break
        if puzzle_input[y+i][x+i] == xmas[i]: occurrences += 0.25
    if occurrences % 1 != 0: occurrences -= occurrences % 1
    # Down
    for i in range(len(xmas)):
        if (y+i) >= len(puzzle_input): break
        if puzzle_input[y+i][x] == xmas[i]: occurrences += 0.25
    if occurrences % 1 != 0: occurrences -= occurrences % 1
    # Down Left
    for i in range(len(xmas)):
        if (x-i) < 0 or (y+i) >= len(puzzle_input): break
        if puzzle_input[y+i][x-i] == xmas[i]: occurrences += 0.25
    if occurrences % 1 != 0: occurrences -= occurrences % 1
    # Left
    for i in range(len(xmas)):
        if (x-i) < 0: break
        if puzzle_input[y][x-i] == xmas[i]: occurrences += 0.25
    if occurrences % 1 != 0: occurrences -= occurrences % 1
    # Left Up
    for i in range(len(xmas)):
        if (x-i) < 0 or (y-i) < 0: break
        if puzzle_input[y-i][x-i] == xmas[i]: occurrences += 0.25
    if occurrences % 1 != 0: occurrences -= occurrences % 1
    # Up
    for i in range(len(xmas)):
        if (y-i) < 0: break
        if puzzle_input[y-i][x] == xmas[i]: occurrences += 0.25
    if occurrences % 1 != 0: occurrences -= occurrences % 1
    # Right Up
    for i in range(len(xmas)):
        if (x+i) >= len(puzzle_input[y]) or (y-i) < 0: break
        if puzzle_input[y-i][x+i] == xmas[i]: occurrences += 0.25
    if occurrences % 1 != 0: occurrences -= occurrences % 1

    return occurrences

total_occurrences = 0
for y in range(len(puzzle_input)):
    for x in range(len(puzzle_input[y])):
        total_occurrences += find_occurrences(x,y)

print(total_occurrences)