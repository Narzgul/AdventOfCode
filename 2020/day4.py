valid = 0
clean_passports = []
fields = []
re_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
with open('day4_input.txt') as f:
    raw_passports = f.read().split('\n\n')
for item in raw_passports:
    clean_passports.append(item.replace("\n", ' ').split(' '))

for item in clean_passports:
    d = dict(i.split(':') for i in item)
    if all(v in d for v in re_fields):
        valid += 1
print(d)
print(valid)
