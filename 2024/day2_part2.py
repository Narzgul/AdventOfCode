with open("inputs/day2_input.txt") as file:
    puzzle_input = file.readlines()

def check_safe(levels):
    if int(levels[0]) < int(levels[1]):
        is_safe = 1
        for i in range(len(levels) - 1):
            if int(levels[i]) >= int(levels[i + 1]) or abs(int(levels[i]) - int(levels[i + 1])) > 3:
                is_safe = 0
                break
        if is_safe > 0:
            return True
    if int(levels[0]) > int(levels[1]):
        is_safe = 1
        for i in range(len(levels) - 1):
            if int(levels[i]) <= int(levels[i + 1]) or abs(int(levels[i]) - int(levels[i + 1])) > 3:
                is_safe = 0
                break
        if is_safe > 0:
            return True

safe_lines = 0
wrg = 0
for report in puzzle_input:
    if check_safe(report.split()):
        safe_lines += 1
    else:
        wrg += 1
        wrg_levels = report.split()
        for j in range(len(wrg_levels)):
            lvs = wrg_levels.copy()
            lvs.pop(j)
            if check_safe(lvs):
                safe_lines += 1
                break

print(safe_lines)