with open("2021/inputs/day1_input.txt") as file:
    input = file.readlines()

total_increases = 0
previous_sum = 10000000
for i in range(len(input)-2):
    sum = int(input[i]) + int(input[i+1]) + int(input[i+2])
    if sum > previous_sum:
        total_increases += 1
    previous_sum = sum

print(total_increases)