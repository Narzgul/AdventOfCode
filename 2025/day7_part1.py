with open("inputs/day7_input.txt") as puzzle_input:
    diagram = []
    for line in puzzle_input:
        diagram.append(list(line.strip()))

    split_count = 0
    for i in range(1, len(diagram)):
        for j in range(len(diagram[i])):
            if diagram[i][j] == "^" and diagram[i - 1][j] == "|":
                diagram[i][j - 1] = "|"
                diagram[i][j + 1] = "|"
                split_count += 1
            if diagram[i][j] == "." and (diagram[i - 1][j] == "|" or diagram[i - 1][j] == "S"):
                diagram[i][j] = "|"

    print(split_count)