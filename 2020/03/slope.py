"""https://adventofcode.com/2020/day/3"""

INPUT = []


with open("input.txt", "r") as read_input:
    INPUT = [line.strip() for line in read_input.read().splitlines()]


def count_trees(puzzle: list, right: int, down: int) -> int:
    """count # in puzzle path"""
    cur = 0
    count = 0
    for i in range(0, len(puzzle), down):
        if puzzle[i][cur] == "#":
            count += 1
        cur = (cur + right) % len(puzzle[0])
    return count


print("Trees: {}".format(count_trees(INPUT, 3, 1)))
print(
    "Composite {}".format(
        count_trees(INPUT, 1, 1)
        * count_trees(INPUT, 3, 1)
        * count_trees(INPUT, 5, 1)
        * count_trees(INPUT, 7, 1)
        * count_trees(INPUT, 1, 2)
    )
)
