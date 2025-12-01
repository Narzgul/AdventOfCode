with open("inputs/day1.txt") as puzzle_input:
    pos = 50
    num_passed_zeros = 0
    for line in puzzle_input:
        direction = line[:1]
        rotation = int(line[1:-1])
        if direction == "R":
            pos = pos + rotation
            while pos >= 100:
                pos = pos - 100
                num_passed_zeros += 1
        elif direction == "L":
            if pos == 0 and rotation > 0:
                num_passed_zeros -= 1
            pos = (pos - rotation)
            while pos < 0:
                pos = pos + 100
                num_passed_zeros += 1
            if pos == 0:
                num_passed_zeros += 1
        print(f"Pos: {pos}, Passed 0s: {num_passed_zeros}")
    print(num_passed_zeros)