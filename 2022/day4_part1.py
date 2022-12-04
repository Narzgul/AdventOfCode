import re

with open("inputs/day4_input.txt") as puzzle_input:
    overlaps = 0

    for line in puzzle_input:
        str_limits = re.findall("[0-9]+", line)
        limits = list(map(int, str_limits))  # Convert to int list
        if (limits[0] <= limits[2] and limits[1] >= limits[3]) or (limits[0] >= limits[2] and limits[1] <= limits[3]):
            overlaps += 1

    print(overlaps)
