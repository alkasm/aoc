from aocd import get_data
from collections import Counter


def data():
    return [int(l) for l in get_data(day=1).splitlines()]


def two_sum(c, sum_to):
    for k, counts in c.items():
        diff = sum_to - k
        if diff in c:
            if k == diff and counts <= 1:
                continue
            return k, diff
    raise ValueError(f"No two values in the iterable sum to {sum_to}.")


def part_one():
    c = Counter(data())
    a, b = two_sum(c, 2020)
    return a * b


def part_two():
    c = Counter(data())
    for v in c:
        c[v] -= 1
        try:
            a, b = two_sum(c, 2020 - v)
            return a * b * v
        except ValueError:
            pass


print(part_one())
print(part_two())
