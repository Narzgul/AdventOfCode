with open("inputs/day2_input.txt") as file:
    puzzle_input = file.readlines()

colors = {'red': 12, 'green': 13, 'blue': 14}

index = 1
sum_ids = 0
for line in puzzle_input:
    print('Game ' + str(index))
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

    print(found_numbers)
    if int(found_numbers['red']) <= colors['red'] and int(found_numbers['green']) <= colors['green'] and int(
            found_numbers['blue']) <= colors['blue']:
        sum_ids += index

    index += 1

print(sum_ids)
