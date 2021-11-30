x = 0
trees = 0
skip = 0
with open('day3_input.txt') as f:
    for line in f:
        if skip == 0:
            if line[x] == '#':
                trees += 1
            x = (x + 1) % 31
        skip = (skip + 1) % 2
print(trees)
