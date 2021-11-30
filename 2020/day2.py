import re

i = 0
with open('day2_input.txt') as f:
    for line in f:
        letter = re.search('[a-z]', line).group(0)
        policies = re.findall('([0-9*]+)', line)
        password = re.search('([a-z]{2,})', line).group(0)
        print(line + '= ' + letter)
        if (password[int(policies[0])-1] == letter) != (password[int(policies[1])-1] == letter):
            i += 1
print(i)
