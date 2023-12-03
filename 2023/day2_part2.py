with open("inputs/day2_input.txt") as file:
    puzzle_input = file.readlines()

colors = {'red': 12, 'green': 13, 'blue': 14}

sum_powers = 0
for line in puzzle_input:
    all_sets = line.split(':')[-1][1:]
    sets = all_sets.split(';')
    found_numbers = {'red': 0, 'green': 0, 'blue': 0}
    for one_set in sets:
        split_one_set = one_set.split()
        for i in range(len(split_one_set)):
            if i % 2 == 0:
                continue

            color = split_one_set[i].strip(',')
            if int(found_numbers[color]) < int(split_one_set[i - 1]):
                found_numbers[color] = split_one_set[i - 1]

    sum_powers += int(found_numbers['red']) * int(found_numbers['green']) * int(found_numbers['blue'])

print(sum_powers)
