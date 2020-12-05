"""From your starting position at the top-left, check the position that is right 3 and down 1.
Then, check the position that is right 3 and down 1 from there, and so on until you go past
the bottom of the map. What do you get if you multiply together the number of trees encountered
on each of the listed slopes?
"""

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
