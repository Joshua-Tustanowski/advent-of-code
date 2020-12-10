from typing import List, Tuple
import re


def part1(inp: str) -> int:
    pass


def load_input_file(filename: str, lines: bool = True):
    with open(filename, 'r') as inp:
        return inp.readlines() if lines else inp.read()


def test_part1():
    inp1 = load_input_file('sample.txt')
    assert part1(inp1) == None

    # inp = load_input_file('input.txt')
    # assert part1(inp) == None


def part2(inp: List[str]) -> int:
    pass


# def test_part2():
    # inp1 = load_input_file('sample.txt')
    # assert part2(inp1) == None

    # inp = load_input_file('input.txt')
    # assert part2(inp) == None
