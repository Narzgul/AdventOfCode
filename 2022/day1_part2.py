import heapq

with open("inputs/day1_input.txt") as file:
    puzzle_input = file.readlines()

largest = [0]
current = 0

for line in puzzle_input:
    if len(line.strip()) != 0:
        current += int(line)
    else:
        heapq.heappush(largest, current * -1)  # -1 to turn into Max Heap
        current = 0

total = 0
for i in range(3):
    total += heapq.heappop(largest) * -1  # -1 cuz Max Heap
    print(total)
