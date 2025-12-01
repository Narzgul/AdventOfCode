with open("inputs/day1_input.txt") as file:
    puzzle_input = file.readlines()

list1 = list2 = []
for line in puzzle_input:
    list1.append(int(line.split('   ')[0]))
    list2.append(int(line.split('   ')[1]))

list1.sort()
list2.sort()

total_distance = 0
for i in range(len(list1)):
    total_distance += abs(list1[i] - list2[i])
print(total_distance)
