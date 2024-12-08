def set_string_at_pos(string, pos, char):
    return string[:pos] + char + string[pos + 1:]

with open("inputs/day6_input.txt") as file:
    puzzle_input = file.readlines()

x = 0
y = 0
for i in range(len(puzzle_input)):
    for j in range(len(puzzle_input[i])):
        if puzzle_input[i][j] == "^":
            x = j
            y = i

direc = 'u'
while True:
    if not (0 <= y < len(puzzle_input) and 0 <= x < len(puzzle_input[y])): break
    puzzle_input[y] = set_string_at_pos(puzzle_input[y], x, "X")
    match direc:
        case 'u':
            y -= 1
            if y >= 0 and puzzle_input[y][x] == "#":
                y += 1
                direc = 'r'
        case 'd':
            y += 1
            if y < len(puzzle_input) and puzzle_input[y][x] == "#":
                y -= 1
                direc = 'l'
        case 'l':
            x -= 1
            if x >= 0 and puzzle_input[y][x] == "#":
                x += 1
                direc = 'u'
        case 'r':
            x += 1
            if x < len(puzzle_input[y]) and puzzle_input[y][x] == "#":
                x -= 1
                direc = 'd'

all_x = 0
for line in puzzle_input: all_x += line.count("X")
print(all_x)