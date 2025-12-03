with open("inputs/day3_input.txt") as puzzle_input:
    total_joltage = 0
    for line in puzzle_input:
        jolt_list = [int(c) for c in line.strip()]
        index_largest = 0
        for i in range(len(jolt_list) - 1):
            if jolt_list[i] > jolt_list[index_largest]:
                index_largest = i
        index_second = index_largest + 1
        for i in range(index_largest + 1, len(jolt_list)):
            if jolt_list[i] > jolt_list[index_second]:
                index_second = i
        total_joltage += 10 * jolt_list[index_largest] + jolt_list[index_second]
    print(total_joltage)