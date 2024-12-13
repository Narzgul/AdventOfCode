import re
from sympy import solve_linear_system, Matrix
from sympy.abc import a, b

with open("inputs/day13_input.txt") as file:
    puzzle_input = file.readlines()

token_sum = 0
for line_num in range(0, len(puzzle_input), 4):
    button_A = re.findall("\\d+", puzzle_input[line_num])
    button_B = re.findall("\\d+", puzzle_input[line_num + 1])
    prize = re.findall("\\d+", puzzle_input[line_num + 2])
    prize[0] = int(prize[0]) + 10000000000000
    prize[1] = int(prize[1]) + 10000000000000
    system = Matrix(((button_A[0], button_B[0], prize[0]), (button_A[1], button_B[1], prize[1])))
    solution = solve_linear_system(system, a, b)
    if solution[a] % 1 == 0 and solution[b] % 1 == 0: token_sum += 3 * solution[a] + solution[b]
print(token_sum)
