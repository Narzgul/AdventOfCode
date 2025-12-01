import datetime
from multiprocessing import Pool

def process_stone(stone, iterations):
    if (stone, iterations) in lookup_table: return  lookup_table[(stone, iterations)]
    if iterations == 0: return 1
    if stone == 0:
        res = process_stone(1, iterations - 1)
    elif len(str(stone)) % 2 == 0:
        cur_stone_str = str(stone)
        res = (process_stone(int(cur_stone_str[:int(len(cur_stone_str) / 2)]), iterations - 1) +
                process_stone(int(cur_stone_str[int(len(cur_stone_str) / 2):]), iterations - 1))
    else: res = process_stone(stone * 2024, iterations - 1)
    lookup_table[(stone, iterations)] = res
    return res

with open("inputs/day11_input.txt") as file:
    stones = [int(x) for x in file.readline().split()]

last_time = datetime.datetime.now()
result_len = 0
lookup_table = {}
for stone in stones:
    result_len += process_stone(stone, 75)
time = datetime.datetime.now()
print("Time taken: " + str(time - last_time) + ", Result: " + str(result_len))