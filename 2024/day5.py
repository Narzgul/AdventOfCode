isRule = True
rules = {}
correct_update_middle_sum = incorrect_update_middle_sum = 0
with open("inputs/day5_input.txt") as file:
    for line in file:
        if line == "\n":
            isRule = False
            continue

        if isRule:
            rule_parts = [int(x) for x in line.split("|")]
            if rules.get(rule_parts[0]) is None:
                rules[rule_parts[0]] = [rule_parts[1]]
            else:
                rules[rule_parts[0]].append(rule_parts[1])
        else:
            update_parts = [int(x) for x in line.split(",")]
            correct_update = True
            for i in range(len(update_parts)):
                for j in range(i + 1, len(update_parts)):
                    if update_parts[j] not in rules.keys(): continue
                    if update_parts[i] in rules[update_parts[j]]:
                        correct_update = False
            if correct_update:
                correct_update_middle_sum += update_parts[int(len(update_parts) / 2)]
            else:
                parts_after = dict.fromkeys(update_parts, 0)
                for part in update_parts:
                    for p in update_parts: parts_after[part] += rules[part].count(p)
                parts_after = sorted(parts_after, key=parts_after.get)
                incorrect_update_middle_sum += parts_after[int(len(parts_after) / 2)]

print("Correct updates: " + str(correct_update_middle_sum))
print("Incorrect updates: " + str(incorrect_update_middle_sum))
