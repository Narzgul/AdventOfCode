import re

def check_equation(result, all_numbers):
    if len(all_numbers) > 2:
        if (check_equation(result - all_numbers[-1], all_numbers[:-1]) + all_numbers[-1] == result or
                check_equation(round(result / all_numbers[-1]), all_numbers[:-1]) * all_numbers[-1] == result):
            return result
    if all_numbers[0] + all_numbers[-1] == result or all_numbers[0] * all_numbers[-1] == result: return result
    return 0

with open("inputs/day7_input.txt") as file:
    sum_of_possible = 0
    for line in file:
        numbers = [int(x) for x in re.findall("[0-9]+", line)]
        sum_of_possible += check_equation(numbers[0], numbers[1:])
print(sum_of_possible)