with open("inputs/day9_input.txt") as file:
    line = file.readline()

id_list = []
for id_num in range(len(line)):
    if (id_num + 1) % 2 == 0:
        for i in range(int(line[id_num])): id_list.append(-1)
    else:
        for i in range(int(line[id_num])): id_list.append(int(id_num / 2))
filesystem_checksum = 0
for i in range(len(id_list)):
    if id_list[i] == -1:
        for j in range(len(id_list) - 1, 0, -1):
            if i >= j: break
            if id_list[j] != -1:
                id_list[i] = id_list[j]
                id_list[j] = -1
                break
    if id_list[i] != -1: filesystem_checksum += i * id_list[i]

print(filesystem_checksum)
