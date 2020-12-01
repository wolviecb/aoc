"""find the two entries that sum to 2020 and then multiply those two numbers together."""
import itertools
from functools import reduce

with open("input.txt", "r") as read_input:
    i = read_input.readlines()
    INPUT = list(map(int, i))


def expense(exps: list, entries: int) -> int:
    """find the two entries that sum to 2020 and then multiply those two numbers together."""
    total = []
    for idx in itertools.combinations(exps, entries):
        if sum(idx) == 2020:
            idxs = [exps.index(number) for number in idx]
            keys = lambda x: exps[x]
            total = [keys(x) for x in idxs]
    return reduce(lambda x, y: x * y, total)


print("{}".format(expense(INPUT, 2)))
print("{}".format(expense(INPUT, 3)))
