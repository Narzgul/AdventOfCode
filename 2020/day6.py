import string

yeses = 0
abc = string.ascii_lowercase
with open('day6_input.txt') as f:
    groups = f.read().split('\n\n')
    for g in groups:
        d = g.split('\n')
        for a in d[0]:
            i = 0
            for b in d:
                if b.__contains__(a):

                    i += 1
            if i == len(d):
                print(d)
                print(a)
                print('----------')
                yeses += 1
print(yeses)
