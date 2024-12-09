with open("inputs/day9_input.txt") as file:
    line = file.readline()

id_list = []
for id_num in range(len(line)):
    if (id_num + 1) % 2 == 0:
        for i in range(int(line[id_num])): id_list.append(-1)
    else:
        for i in range(int(line[id_num])): id_list.append(int(id_num / 2))

filesystem_checksum = 0
for i in range(len(id_list) - 1, -1, -1):
    if id_list[i] != -1:
        file_len = id_list.count(id_list[i])
        i = i - file_len + 1
        start_free = len(id_list)
        for j in range(len(id_list)):
            if id_list[j:j + file_len] == [-1 for x in range(file_len)]:
                start_free = j
                break
        if i <= start_free: continue
        for k in range(file_len):
            id_list[start_free + k] = id_list[i + k]
            id_list[i + k] = -1
for i in range(len(id_list)):
    if id_list[i] != -1: filesystem_checksum += i * id_list[i]

print(filesystem_checksum)
