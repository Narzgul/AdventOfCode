import datetime
from multiprocessing import Pool


def process_stones_len(my_stones, iterations):
    for j in range(iterations):
        my_stone_index = 0
        # set current time
        while my_stone_index < len(my_stones):
            if my_stones[my_stone_index] == 0: my_stones[my_stone_index] = 1
            elif len(str(my_stones[my_stone_index])) % 2 == 0:
                cur_stone_str = str(my_stones[my_stone_index])
                my_stones[my_stone_index] = int(cur_stone_str[:int(len(cur_stone_str) / 2)])
                my_stones.insert(my_stone_index + 1, int(cur_stone_str[int(len(cur_stone_str) / 2):]))
                my_stone_index += 1
            else: my_stones[my_stone_index] = my_stones[my_stone_index] * 2024
            my_stone_index += 1
    return len(my_stones)

def process_stones(my_stones, iterations):
    for j in range(iterations):
        my_stone_index = 0
        # set current time
        while my_stone_index < len(my_stones):
            if my_stones[my_stone_index] == 0: my_stones[my_stone_index] = 1
            elif len(str(my_stones[my_stone_index])) % 2 == 0:
                cur_stone_str = str(my_stones[my_stone_index])
                my_stones[my_stone_index] = int(cur_stone_str[:int(len(cur_stone_str) / 2)])
                my_stones.insert(my_stone_index + 1, int(cur_stone_str[int(len(cur_stone_str) / 2):]))
                my_stone_index += 1
            else: my_stones[my_stone_index] = my_stones[my_stone_index] * 2024
            my_stone_index += 1
    return my_stones


with open("inputs/day11_input.txt") as file:
    stones = [int(x) for x in file.readline().split()]

last_time = datetime.datetime.now()
with Pool(processes=12) as pool:
    stones = process_stones(stones, 20)
    process_results = [pool.apply_async(process_stones_len, (stones[int(len(stones) / 12 * i):int(len(stones) / 12 * (i+1))], 5)) for i in range(12)]
    result_len = 0
    for res in process_results: result_len += res.get()
time = datetime.datetime.now()
print("Time taken: " + str(time - last_time) + ", Result: " + str(result_len))