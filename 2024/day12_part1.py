def find_region(plant, current_region, x, y):
    current_region.append((x, y))
    if x + 1 < len(puzzle[y]) and puzzle[y][x + 1] == plant and (x + 1, y) not in current_region:
        current_region.extend(find_region(plant, current_region, x + 1, y))  # Right
    if y + 1 < len(puzzle) and puzzle[y + 1][x] == plant and (x, y + 1) not in current_region:
        current_region.extend(find_region(plant, current_region, x, y + 1))  # Down
    if x - 1 >= 0 and puzzle[y][x - 1] == plant and (x - 1, y) not in current_region:
        current_region.extend(find_region(plant, current_region, x - 1, y))  # Left
    if y - 1 >= 0 and puzzle[y - 1][x] == plant and (x, y - 1) not in current_region:
        current_region.extend(find_region(plant, current_region, x, y - 1))  # Up

    for point in current_region:
        current_region.remove(point)
        if point not in current_region: current_region.insert(0, point)

    return current_region

def get_perimeter(region_to_perimeter):
    perimeter = 0
    for point in region_to_perimeter:
        if (point[0] + 1, point[1]) not in region_to_perimeter: perimeter += 1
        if (point[0], point[1] + 1) not in region_to_perimeter: perimeter += 1
        if (point[0] - 1, point[1]) not in region_to_perimeter: perimeter += 1
        if (point[0], point[1] - 1) not in region_to_perimeter: perimeter += 1
    return perimeter

with open("inputs/day12_input.txt") as file:
    puzzle = file.readlines()
regions = []
for i in range(len(puzzle)):
    for j in range(len(puzzle[i]) - 1):  # -1 because of \n
        contained = False
        for region in regions: # contained = contained or (j, i) in region
            if (j, i) in region: contained = True
        if not contained: regions.append(find_region(puzzle[i][j], [(j, i)], j, i))
print(len(regions))

total_price = 0
for region in regions:
    total_price += get_perimeter(region) * len(region)
print(total_price)