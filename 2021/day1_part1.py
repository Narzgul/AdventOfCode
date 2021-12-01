with open("2021/inputs/day1_input.txt") as file:
    input = file.readlines()

total_increases = 0
previous = 10000000
for line in input:
    if int(line) > previous:
        total_increases += 1
    previous = int(line)

print(total_increases)