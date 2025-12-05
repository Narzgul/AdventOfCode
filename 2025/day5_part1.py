with open("inputs/day5_input.txt") as puzzle_input:
    ranges = []
    availibles = []
    # Parse input
    for line in puzzle_input:
        if '-' in line:
            split_line = line.split('-')
            ranges.append((int(split_line[0]), int(split_line[1])))
        elif line != '\n':
            availibles.append(int(line))

    fresh_num = 0
    for prod_id in availibles:
        for fresh in ranges:
            if fresh[0] <= prod_id <= fresh[1]:
                fresh_num += 1
                break

    print(fresh_num)