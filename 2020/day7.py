import re


def bag(string, num):
    temp = {}
    temp['name'] = re.findall('[a-z]+ [a-z]+ [a-z]+', string)[num]
    temp['amount'] = re.findall('[1-9]+', string)[num-1]
    print(temp.get('name'))


rules = []
with open('day7_input.txt') as f:
    raw_rules = f.read().split('\n')
for r in raw_rules:
    tem_dict = dict(bag=re.search('[a-z]+ [a-z]+ [a-z]+', r).group(0))
    name_bags = re.findall('[1-9]+', r)
    # tem_dict['contains'] = dict([i] for i in range(len(name_bags)))
    rules.append(tem_dict)
    bag(r, 0)
# amount=re.search('[1-9]', r),
print(rules)
