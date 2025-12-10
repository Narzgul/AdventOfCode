import numpy as np

with open("inputs/day6_input.txt") as puzzle_input:
    char_array = []
    for problem in puzzle_input:
        char_line = []
        for char in problem[:-1]:
            char_line.append(char)
        char_array.append(char_line)
    for i in range(len(char_array[0]) - len(char_array[-1])):
        char_array[-1].append(" ")
    np_char_array = np.array(char_array)

    sep_columns = [-1]
    for i in range(len(np_char_array[0])):
        is_sep = True
        for j in range(len(np_char_array)):
            if np_char_array[j][i] != " ":
                is_sep = False
                break
        if is_sep:
            sep_columns.append(i)
    sep_columns.append(len(np_char_array[0]))

    problems = []
    for i in range(len(sep_columns) - 1):
        problems.append(np_char_array[:, sep_columns[i] + 1:sep_columns[i+1]])

    total = 0
    for problem in problems:
        if "+" in problem[-1]:
            for column in problem.T:
                comp = ""
                for num in column[:-1]:
                    if num != " ":
                        comp += num
                total += int(comp)
        else:
            subtotal = 0
            for column in problem.T:
                comp = ""
                for num in column[:-1]:
                    if num != " ":
                        comp += num
                if subtotal == 0:
                    subtotal = int(comp)
                else:
                    subtotal *= int(comp)
            total += subtotal
    print(total)