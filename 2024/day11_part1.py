import datetime

with open("inputs/day11_input.txt") as file:
    stones = [int(x) for x in file.readline().split()]
    for i in range(25):
        stone_index = 0
        while stone_index < len(stones):
            if stones[stone_index] == 0: stones[stone_index] = 1
            elif len(str(stones[stone_index])) % 2 == 0:
                cur_stone_str = str(stones[stone_index])
                stones[stone_index] = int(cur_stone_str[:int(len(cur_stone_str) / 2)])
                stones.insert(stone_index + 1, int(cur_stone_str[int(len(cur_stone_str) / 2):]))
                stone_index += 1
            else: stones[stone_index] = stones[stone_index] * 2024
            stone_index += 1
print(len(stones))