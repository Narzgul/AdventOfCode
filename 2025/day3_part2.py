with open("inputs/day3_input.txt") as puzzle_input:
    total_joltage = 0
    for line in puzzle_input:
        jolt_list = [int(c) for c in line.strip()]
        last_index = -1
        last_total = total_joltage
        for j in range(11, -1, -1):
            index_largest = last_index + 1
            for i in range(last_index + 1, len(jolt_list) - j):
                if jolt_list[i] > jolt_list[index_largest]:
                    index_largest = i
            total_joltage += jolt_list[index_largest] * 10**j
            last_index = index_largest
    print(total_joltage)