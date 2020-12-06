"""https://adventofcode.com/2020/day/2"""
from typing import Callable


with open("input.txt", "r") as read_input:
    INPUT = list(map(str, read_input.readlines()))


def validate(passwords: list, check_type: Callable[[str, str, int, int], bool]) -> int:
    """Validate takes the list of passwords/policies and break it into the required fields(str)
    required character(str) and password(str), required fields if then broken into two integers
    that represent the required fields
    Then if validates the passwords using the check_type function"""
    count = 0
    for password in passwords:
        req, char, pwd = password.split(" ")
        low, high = list(map(int, req.split("-")))
        char = char.strip(":")
        if check_type(pwd, char, low, high):
            count += 1
    return count


def check_length(pwd: str, char: str, low: int, high: int) -> bool:
    """Check_length returns True if pwd contains char in between low and high times"""
    return low <= pwd.count(char) <= high


def check_char(pwd: str, char: str, low: int, high: int) -> bool:
    """Check_char return True if pwd contains char in the field
    low OR in the field high, but not both"""
    return (pwd[low - 1] == char) != (pwd[high - 1] == char)


print(validate(INPUT, check_length))
print(validate(INPUT, check_char))
