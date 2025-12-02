with open("inputs/day2_input.txt") as puzzle_input:
    sum_invalid_ids = 0
    for line in puzzle_input:
        ranges = line.split(sep=",")
        for prod_range in ranges:
            ids_start_end = prod_range.split(sep="-")
            for prod_id in range(int(ids_start_end[0]), int(ids_start_end[1]) + 1):
                prod_id_str = str(prod_id)
                for i in range(1, len(prod_id_str)):
                    if prod_id_str == prod_id_str[:i] * int(len(prod_id_str) / i):
                        sum_invalid_ids += prod_id
                        break
    print(sum_invalid_ids)