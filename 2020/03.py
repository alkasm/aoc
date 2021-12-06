from aocd import get_data


def part_one(data, slope):
    right, down = slope
    pos_x = 0
    pos_y = 0

    height = len(data)
    width = len(data[0])

    count = 0
    while True:
        if data[pos_y][pos_x % width] == "#":
            count += 1
        pos_x += right
        pos_y += down
        if pos_y >= height:
            break
    return count


def part_two(data, slopes):
    total = 1
    for slope in slopes:
        total *= part_one(data, slope)
    return total


data = get_data(day=3).splitlines()

print(part_one(data, (3, 1)))
print(part_two(data, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
