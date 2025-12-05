import itertools

def find_next_moveable(roll_map):
    for i in range(len(roll_map)):
        for j in range(len(roll_map[i])):
            if roll_map[i][j] == '@':
                occupied_neighbours = -1 # -1 because 0,0 is always occupied
                for comb in itertools.product([-1, 0, 1], repeat=2):
                    if (0 <= comb[0] + i < len(roll_map)) and (0 <= comb[1] + j < len(roll_map[i])):
                        if roll_map[comb[0] + i][comb[1] + j] == '@':
                            occupied_neighbours += 1
                if occupied_neighbours < 4:
                    return i, j
    return None


with open("inputs/day4_input.txt") as puzzle_input:
    roll_map = []
    for line in puzzle_input:
        roll_map.append(list(line.strip()))

    removed_rolls = 0
    while find_next_moveable(roll_map) is not None:
        indexes = find_next_moveable(roll_map)
        roll_map[indexes[0]][indexes[1]] = '.'
        removed_rolls += 1

    print(removed_rolls)