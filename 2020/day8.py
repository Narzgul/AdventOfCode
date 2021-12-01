with open("2020/inputs/day8_input.txt") as file:
    all_lines = file.readlines()

accumulator = 0

visited = []
current_line_nr = 0
while current_line_nr not in visited:
    visited.append(current_line_nr)
    line = all_lines[current_line_nr]

    print(str(current_line_nr) + ": " + line.strip())
    if line[:3] == "acc":
        accumulator += int(line[4:])
    elif line[:3] == "jmp":
        current_line_nr += int(line[4:]) -1
    
    current_line_nr += 1

print(accumulator)
print(current_line_nr)