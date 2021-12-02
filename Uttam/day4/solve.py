from typing import List, Tuple
import re
import string


def load_input_file(filename: str, blocks: bool = True):
    with open(filename, "r") as inp:
        return inp.read().split("\n\n") if blocks else inp.read()


def check_attributes1(attributes: set) -> bool:
    if len(attributes) == 8 or (len(attributes) == 7 and "cid" not in attributes):
        return True
    return False


def part1(blocks: List[str]) -> int:
    no_of_valid_passports = 0
    for block in blocks:
        block = block.replace("\n", " ")
        pairs = block.split(" ")
        attributes = {pair.split(":")[0] for pair in pairs}
        if check_attributes1(attributes):
            no_of_valid_passports += 1
    return no_of_valid_passports


def test_part1():
    inp1 = load_input_file("sample.txt")
    assert part1(inp1) == 2

    inp = load_input_file("input.txt", blocks=True)
    assert part1(inp) == 254


def check_attributes2(fields: dict) -> bool:
    """
    You can continue to ignore the cid field, but each other field has strict rules about what values are
    valid for automatic validation:

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most solutions_2020.
    eyr (Expiration Year) - four digits; at least solutions_2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    if len(fields) < 7:
        return False

    try:
        # Years
        assert len(fields["byr"]) == 4 and (1920 <= int(fields["byr"]) <= 2002)
        assert len(fields["iyr"]) == 4 and (2010 <= int(fields["iyr"]) <= 2020)
        assert len(fields["eyr"]) == 4 and (2020 <= int(fields["eyr"]) <= 2030)

        # Height
        height = fields["hgt"]
        if height.endswith("cm"):
            assert 150 <= int(height[:-2]) <= 193
        elif height.endswith("in"):
            assert 59 <= int(height[:-2]) <= 76
        else:
            return False

        # Colours
        assert re.match(r"#[0-9a-f]{6}", fields["hcl"])
        assert fields["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

        # Passport ID
        assert len(fields["pid"]) == 9
        assert set(fields["pid"]) <= set(string.digits)

        return True
    except (AssertionError, KeyError):
        return False


def part2(blocks: List[str]) -> int:
    no_of_valid_passports = 0
    for block in blocks:
        attributes = {}
        for pair in block.replace("\n", " ").split(" "):
            attr, val = pair.split(":")
            attributes[attr] = val

        if check_attributes2(attributes):
            no_of_valid_passports += 1
    return no_of_valid_passports


def test_part2():
    invalid_ones = load_input_file("p2_invalid.txt")
    assert part2(invalid_ones) == 0

    valid_ones = load_input_file("p2_valid.txt")
    assert part2(valid_ones) == 4

    inp = load_input_file("input.txt")
    assert part2(inp) == 184
