with open("inputs/day7_input.txt") as puzzle_input:
    diagram = []
    for line in puzzle_input:
        diagram.append(list(line.strip()))

    splits_lookup = {}

    def rec_splits(x, y):
        while diagram[x][y] == "." and x < len(diagram) - 1:
            x += 1
        if diagram[x][y] == "^":
            if (x, y) in splits_lookup:
                return splits_lookup[(x, y)]
            else:
                splits_lookup[(x, y)] = rec_splits(x, y - 1) + rec_splits(x, y + 1)
                return splits_lookup[(x, y)]
        else:
            return 1

    for i in range(len(diagram[0])):
        if diagram[0][i] == "S":
            print(rec_splits(1, i))
            break