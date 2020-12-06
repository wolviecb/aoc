"""https://adventofcode.com/2020/day/4"""

INPUT = []
with open("input.txt", "r") as read_input:
    INPUT = "".join(read_input.readlines()).replace("\n", " ").split("  ")

REQUIRED = {
    "byr": {"min": 1920, "max": 2002},
    "iyr": {"min": 2010, "max": 2020},
    "eyr": {"min": 2020, "max": 2030},
    "hgt": {"cm":{"min": 150, "max":193}, "in":{"min":59, "max":76}},
    "hcl": "",
    "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": ""
}


def validate(data: list) -> int:
    """Badly validates passport data"""
    counter = 0
    passports = parse(data)
    for passport in passports:
        if len(set(REQUIRED).intersection(passport)) == 7:
            counter += 1
    return counter

def hell_validate(data: list) -> int:
    """Validates passport data against the REQUIRED dictionary"""
    counter = 0
    passports = parse(data)
    for passport in passports:
        try:
            if (
                    REQUIRED["byr"]["min"] <= int(passport["byr"]) <= REQUIRED["byr"]["max"] and
                    REQUIRED["iyr"]["min"] <= int(passport["iyr"]) <= REQUIRED["iyr"]["max"] and
                    REQUIRED["eyr"]["min"] <= int(passport["eyr"]) <= REQUIRED["eyr"]["max"] and
                    (
                        REQUIRED["hgt"][passport["hgt"].rsplit()[0][-2:]]["min"] <=
                        int(passport["hgt"][:-2]) <=
                        REQUIRED["hgt"][passport["hgt"].rsplit()[0][-2:]]["max"]
                    ) and
                    passport["hcl"][0] == "#" and
                    int(passport["hcl"][1:7], 16) is not ValueError and
                    passport["ecl"] in REQUIRED["ecl"] and
                    int(passport["pid"]) is not ValueError and
                    len(passport["pid"]) == 9
                ):
                counter += 1
        except (KeyError, ValueError):
            continue
    return counter

def parse(data: list) -> list:
    """Parses passport data and generates a list dicts"""
    passports = []
    for row in data:
        passport = {x[0]:x[1] for x in [i.split(':') for i in row.split()]}
        passport.pop('cid', None)
        passports.append(passport)
    return passports

print("{}".format(validate(INPUT)))
print("{}".format(hell_validate(INPUT)))
