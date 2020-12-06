"""https://adventofcode.com/2020/day/6"""
from functools import reduce
from typing import Callable


INPUT = []
with open("input.txt") as read_input:
    INPUT = [ line.splitlines() for line in read_input.read().split("\n\n")]


def forms(answers: list, check_type: Callable[[list], int]) -> int:
    """Gets a list of answers and pass each groups to check_type and sums the results"""
    counter = 0
    for answer in answers:
        counter += check_type(answer)
    return counter


def count(answer: list) -> int:
    """For each group, count the number of questions to which anyone answered yes"""
    return len(set("".join(answer)))


def dupes(answer: list) -> int:
    """For each group, count the number of questions to which everyone answered yes"""
    return len(reduce(lambda x, y: x & y, map(set, answer)))


print("{}".format(forms(INPUT, count)))
print("{}".format(forms(INPUT, dupes)))
