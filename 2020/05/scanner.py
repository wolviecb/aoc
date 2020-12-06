"""https://adventofcode.com/2020/day/5"""


def row(data: list, node: str) -> list:
    """returns a list equals to half of data and returns the half based on node"""
    if node in ("F", "L"):
        return data[: int(len(data) / 2)]
    if node in ("B", "R"):
        return data[int(len(data) / 2) :]
    return LookupError


def search(index: str, kind: list) -> int:
    """Search the index on kind"""
    for node in index:
        while len(node) >= 1:
            kind = row(kind, node[:1])
            node = node[1:]
    return kind[0]


def parse(data: list) -> list:
    """parses data and returns a list of occupied 'seats'"""
    ids = []
    for node in data:
        node = node.strip()
        ids.append(search(node[:-3], range(128)) * 8 + search(node[-3:], range(8)))
    return ids


with open("input.txt", "r") as read_input:
    LINES = read_input.readlines()
    INPUT = list(map(str, LINES))
    INPUT = parse(INPUT)
    INPUT.sort()


def first_consecutive(lst: list) -> int:
    """returns the first non consecutive int in lst"""
    for i, j in enumerate(lst, lst[0]):
        if i != j:
            return j - 1
    return False


print("answer 1: {}".format(max(INPUT)))
print("answer 2: {}".format(first_consecutive(INPUT)))
