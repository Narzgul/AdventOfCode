import re

room = [[0 for y in range(101)] for x in range(103)]
with open("inputs/day14_input.txt") as file:
    for line in file.readlines():
        nums = [int(x) for x in re.findall("-?\\d+", line)]
        pos = [nums[0], nums[1]]
        vel = (nums[2], nums[3])
        for i in range(100):
            pos[0] = (pos[0] + vel[0]) % len(room[0])
            pos[1] = (pos[1] + vel[1]) % len(room)
        room[pos[1]][pos[0]] += 1

safety_factor = 1
current_quadrant = 0
for i in range(int(len(room) / 2)):
    for j in range(int(len(room[i]) / 2)): current_quadrant += room[i][j]
safety_factor *= current_quadrant
current_quadrant = 0
for i in range(int(len(room) / 2) + 1, len(room)):
    for j in range(int(len(room[i]) / 2)): current_quadrant += room[i][j]
safety_factor *= current_quadrant
current_quadrant = 0
for i in range(int(len(room) / 2)):
    for j in range(int(len(room[i]) / 2) + 1, len(room[i])): current_quadrant += room[i][j]
safety_factor *= current_quadrant
current_quadrant = 0
for i in range(int(len(room) / 2) + 1, len(room)):
    for j in range(int(len(room[i]) / 2) + 1, len(room[i])): current_quadrant += room[i][j]
safety_factor *= current_quadrant
print(safety_factor)
