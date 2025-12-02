with open("inputs/day1_input.txt") as puzzle_input:
    pos = 50
    num_zeros = 0
    for line in puzzle_input:
        direction = line[:1]
        rotation = int(line[1:-1])
        if direction == "R":
            pos = (pos + rotation) % 100
        elif direction == "L":
            pos = (pos - rotation) % 100
        if pos == 0:
            num_zeros += 1
    print(num_zeros)