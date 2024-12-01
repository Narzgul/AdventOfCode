with open("inputs/day1_input.txt") as file:
    puzzle_input = file.readlines()

list1 = []
list2 = []
for line in puzzle_input:
    list1.append(int(line.split('   ')[0]))
    list2.append(int(line.split('   ')[1]))

similarity_score = 0
for i in list1:
    similarity_score += i * list2.count(i)

print(similarity_score)