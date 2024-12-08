def set_string_at_pos(string, pos, char):
    return string[:pos] + char + string[pos + 1:]


with open("inputs/day8_input.txt") as file:
    puzzle_input = file.readlines()

all_antennas = {}
for y in range(len(puzzle_input)):
    for x in range(len(puzzle_input[y])):
        if puzzle_input[y][x] not in ".\n#":
            if all_antennas.get(puzzle_input[y][x]) is None: all_antennas[puzzle_input[y][x]] = []
            all_antennas[puzzle_input[y][x]].append((x, y))

print(all_antennas)
for freq in all_antennas:
    for antenna1 in all_antennas[freq]:
        for antenna2 in all_antennas[freq]:
            if antenna1 != antenna2:
                vector = (antenna1[0] - antenna2[0], antenna1[1] - antenna2[1])
                antinode = (antenna1[0] + vector[0], antenna1[1] + vector[1])
                if 0 <= antinode[1] < len(puzzle_input) and 0 <= antinode[0] < len(puzzle_input[antinode[1]]):
                    if puzzle_input[antinode[1]][antinode[0]] != "\n":
                        puzzle_input[antinode[1]] = set_string_at_pos(puzzle_input[antinode[1]], antinode[0], "#")

all_antinodes = 0
for line in puzzle_input:
    for char in line:
        if char == "#": all_antinodes += 1

print(all_antinodes)
