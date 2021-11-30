
numbers = []
with open('day1_input.txt') as f:
    numbers = list(map(int, f.readlines()))

for i in numbers:
    for j in numbers:
        for k in numbers:
            if i + j + k == 2020:
                print(i)
                print(j)
                print(k)
                print('--------')
                exit(0)