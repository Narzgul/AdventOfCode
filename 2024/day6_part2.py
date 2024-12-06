def set_string_at_pos(string, pos, char):
    return string[:pos] + char + string[pos + 1:]

with open("inputs/day6_input.txt") as file:
    puzzle_input = file.readlines()

x = y = initial_x = initial_y = 0
for i in range(len(puzzle_input)):
    for j in range(len(puzzle_input[i])):
        if puzzle_input[i][j] == "^":
            x = initial_x = j
            y = initial_y = i

direction = 'u'
while 0 <= y < len(puzzle_input) and 0 <= x < len(puzzle_input[y]):
    match direction:
        case 'u':
            puzzle_input[y] = set_string_at_pos(puzzle_input[y], x, "U")
            y -= 1
            if y >= 0 and puzzle_input[y][x] == "#":
                y += 1
                direction = 'r'
        case 'd':
            puzzle_input[y] = set_string_at_pos(puzzle_input[y], x, "D")
            y += 1
            if y < len(puzzle_input) and puzzle_input[y][x] == "#":
                y -= 1
                direction = 'l'
        case 'l':
            puzzle_input[y] = set_string_at_pos(puzzle_input[y], x, "L")
            x -= 1
            if x >= 0 and puzzle_input[y][x] == "#":
                x += 1
                direction = 'u'
        case 'r':
            puzzle_input[y] = set_string_at_pos(puzzle_input[y], x, "R")
            x += 1
            if x < len(puzzle_input[y]) and puzzle_input[y][x] == "#":
                x -= 1
                direction = 'd'

def check_loop(block_x, block_y, x, y, input_array):
    direction = 'U'
    puzzle_stacked = [input_array.copy(), input_array.copy()]
    puzzle_stacked[0][block_y] = set_string_at_pos(puzzle_stacked[0][block_y], block_x, "#")
    while 0 <= y < len(puzzle_stacked[0]) and 0 <= x < len(puzzle_stacked[0][y]):
        if puzzle_stacked[0][y][x] in ["u", "d", "l", "r"]:
            puzzle_stacked[1][y] = set_string_at_pos(puzzle_stacked[1][y], x, puzzle_stacked[0][y][x])
        match direction:
            case 'U':
                puzzle_stacked[0][y] = set_string_at_pos(puzzle_stacked[0][y], x, "u")
                y -= 1
                if y >= 0:
                    if "u" in [puzzle_stacked[0][y][x], puzzle_stacked[1][y][x]]: return True
                    if puzzle_stacked[0][y][x] == "#":
                        y += 1
                        direction = 'R'
                        if puzzle_stacked[0][y][x] == "r": return True
            case 'D':
                puzzle_stacked[0][y] = set_string_at_pos(puzzle_stacked[0][y], x, "d")
                y += 1
                if y < len(puzzle_stacked[0]):
                    if "d" in [puzzle_stacked[0][y][x], puzzle_stacked[1][y][x]]: return True
                    if puzzle_stacked[0][y][x] == "#":
                        y -= 1
                        direction = 'L'
                        if puzzle_stacked[0][y][x] == "l": return True
            case 'L':
                puzzle_stacked[0][y] = set_string_at_pos(puzzle_stacked[0][y], x, "l")
                x -= 1
                if x >= 0:
                    if "l" in [puzzle_stacked[0][y][x], puzzle_stacked[1][y][x]]: return True
                    if puzzle_stacked[0][y][x] == "#":
                        x += 1
                        direction = 'U'
                        if puzzle_stacked[0][y][x] == "u": return True
            case 'R':
                puzzle_stacked[0][y] = set_string_at_pos(puzzle_stacked[0][y], x, "r")
                x += 1
                if x < len(puzzle_stacked[0]):
                    if "r" in [puzzle_stacked[0][y][x], puzzle_stacked[1][y][x]]: return True
                    if puzzle_stacked[0][y][x] == "#":
                        x -= 1
                        direction = 'D'
                        if puzzle_stacked[0][y][x] == "d": return True
    return False

amount_blocks = 0
for i in range(len(puzzle_input)):
    for j in range(len(puzzle_input[i])):
        if puzzle_input[i][j] in ["U", "D", "L", "R"] and check_loop(j, i, initial_x, initial_y, puzzle_input):
            amount_blocks += 1

print(amount_blocks)