with open("inputs/day3_input.txt") as file:
    puzzle_input = file.readlines()

all_chars = []
for line in puzzle_input:
    for char in line:
        if not all_chars.__contains__(char):
            all_chars.append(char)

all_chars.sort()
print(all_chars)
for char in all_chars:
    print(char, end='')
