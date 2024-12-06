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
    if y >= len(puzzle_input) or y < 0 or x >= len(puzzle_input[y]) or x < 0: break
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

amount_x = 0
for i in range(len(puzzle_input)):
    for j in range(len(puzzle_input[i])):
        if puzzle_input[i][j] == "X": amount_x += 1

print(amount_x)