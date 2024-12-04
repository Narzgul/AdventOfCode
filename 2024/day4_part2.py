with open("inputs/day4_input.txt") as file:
    input = file.readlines()

total_occurrences = 0
for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] != "A": continue
        if (x+1) >= len(input[y]) or (y + 1) >= len(input) or min(x - 1, y - 1) < 0: continue
        if input[y-1][x-1] == "M" and input[y+1][x+1] == "S" and input[y-1][x+1] == "M" and input[y+1][x-1] == "S":
            total_occurrences += 1
        if input[y-1][x-1] == "M" and input[y+1][x+1] == "S" and input[y-1][x+1] == "S" and input[y+1][x-1] == "M":
            total_occurrences += 1
        if input[y-1][x-1] == "S" and input[y+1][x+1] == "M" and input[y-1][x+1] == "M" and input[y+1][x-1] == "S":
            total_occurrences += 1
        if input[y-1][x-1] == "S" and input[y+1][x+1] == "M" and input[y-1][x+1] == "S" and input[y+1][x-1] == "M":
            total_occurrences += 1

print(total_occurrences)