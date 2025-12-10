import numpy as np

with open("inputs/day6_input.txt") as puzzle_input:
    problems = []
    for line in puzzle_input:
        problems.append(" ".join(line.split()).split())

    np_problems = np.array(problems)
    np_problems = np_problems.transpose()

    total = 0
    for line in np_problems:
        line_total = 0
        for num in line:
            if num not in "+*":
                if line[-1] == "+":
                    line_total += int(num)
                if line[-1] == "*":
                    if line_total != 0:
                        line_total *= int(num)
                    else:
                        line_total = int(num)
        total += line_total
    print(total)