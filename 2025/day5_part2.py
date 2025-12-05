with open("inputs/day5_input.txt") as puzzle_input:
    ranges = []
    # Parse input
    for line in puzzle_input:
        if '-' in line:
            split_line = line.split('-')
            ranges.append((int(split_line[0]), int(split_line[1])))

    # Remove overlaps
    ranges.sort()
    for i in range(len(ranges)):
        for j in range(i + 1, len(ranges)):
            if ranges[i][1] >= ranges[j][0]:
                ranges[j] = (ranges[i][1] + 1, ranges[j][1])

    possible_fresh = 0
    for fresh in ranges:
        if fresh[0] <= fresh[1]:
            possible_fresh += fresh[1] - fresh[0] + 1

    print(possible_fresh)