import math

with open("2021/inputs/day3_input.txt") as file:
    input = file.readlines()

def invertBits(num):
    b_dict = {'0': '1', '1': '0'} # create a dictionary
    inverse_s = ''
    
    for i in num:
        inverse_s += b_dict[i]

    return inverse_s

gamma = ""
epsilon = ""
for i in range(12):
    tmp = 0
    for line in input:
        tmp += int(line[i])
    row = int(round(tmp / len(input)))
    gamma += str(row)
epsilon = invertBits(gamma)

print(gamma)
print(epsilon)
print(int(gamma, 2) * int(epsilon, 2))