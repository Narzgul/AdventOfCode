seat_ids = []
columns = [0, 8]

with open('day5_input.txt') as f:
    for line in f:
        rows = [0, 128]
        columns = [0, 8]
        for c in line:
            if c == 'F':
                rows[1] = (rows[1] + rows[0]) / 2
                # print(rows)
            elif c == 'B':
                rows[0] = (rows[1] + rows[0]) / 2
                # print(rows)
            elif c == 'L':
                columns[1] = (columns[1] + columns[0]) / 2
            elif c == 'R':
                columns[0] = (columns[1] + columns[0]) / 2
        rows[1] -= 1
        columns[1] -= 1
        # if (rows[0] * 8) + columns[0] > seat_id:
        #     seat_id = (rows[0] * 8) + columns[0]
        seat_ids.append((rows[0] * 8) + columns[0])
        # print(rows)
        # print(columns)
        # print('-----------')
print(seat_ids)
for i in range(1000):
    if i not in seat_ids:
        if i-1 in seat_ids and i+1 in seat_ids:
            print(i)
