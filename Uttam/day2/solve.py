from typing import List, Tuple
import re
from collections import Counter

regex_pattern = r'(\d+)-(\d+) (\w): (\w+)'


def load_input_file(filename: str, lines: bool = True):
    with open(filename, 'r') as inp:
        return inp.readlines() if lines else inp.read()


def parse_line(line: str) -> Tuple[int, int, str, str]:
    groups = re.search(regex_pattern, line).groups()
    return int(groups[0]), int(groups[1]), groups[2], groups[3]


def is_password_valid(min_: int, max_: int, char: str, password: str) -> bool:
    return min_ <= Counter(password)[char] <= max_


def part1(inp: List[str]) -> int:
    no_of_valid_passwords = 0
    for line in inp:
        if is_password_valid(*parse_line(line)):
            no_of_valid_passwords += 1
    return no_of_valid_passwords


def test_part1():

    assert is_password_valid(*parse_line('1-3 a: abcde'))
    assert not is_password_valid(*parse_line('1-3 b: cdefg'))
    assert is_password_valid(*parse_line('2-9 c: ccccccccc'))
    # assert part1(inp1) == 514579

    inp = load_input_file('input.txt', lines=True)
    assert part1(inp) == 410


def is_password_valid2(pos1: int, pos2: int, char: str, password: str) -> bool:
    return sum([password[pos1-1] == char, password[pos2-1] == char]) == 1


def part2(inp: List[str]) -> int:
    no_of_valid_passwords = 0
    for line in inp:
        if is_password_valid2(*parse_line(line)):
            no_of_valid_passwords += 1
    return no_of_valid_passwords


def test_part2():
    inp = load_input_file('input.txt', lines=True)
    assert part2(inp) == 694
