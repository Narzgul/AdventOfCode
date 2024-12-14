import re

with open("inputs/day14_input.txt") as file:
    pos = {}
    vel = {}
    for line in file.readlines():
        nums = [int(x) for x in re.findall("-?\\d+", line)]
        pos[line] = [nums[0], nums[1]]
        vel[line] = (nums[2], nums[3])
    for i in range(10000):
        room = [[0 for y in range(101)] for x in range(103)]
        for v in vel.keys():
            pos[v][0] = (pos[v][0] + vel[v][0]) % len(room[0])
            pos[v][1] = (pos[v][1] + vel[v][1]) % len(room)
            room[pos[v][1]][pos[v][0]] += 1
        streak = 0
        for y in range(len(room)):
            for x in room[y]:
                if x > 0: streak += 1
                else: streak = 0
                if streak > 31: print(i + 1)
