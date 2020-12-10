from typing import List, Tuple
import re
from itertools import combinations


def part1(inp: List[int], preamble_length: int) -> int:
    for i in range(len(inp) - preamble_length + 1):
        window = inp[i:i+preamble_length]
        number = inp[i+preamble_length]
        # print('\nNumber: {}. Window: {}'.format(number, window))

        # Find number which isn't the sum of two numbers in the window
        if number not in (sum(pair) for pair in combinations(window, 2)):
            return number


def load_input_file(filename: str):
    with open(filename, 'r') as inp:
        return [int(i) for i in inp.readlines()]


def test_part1():
    inp1 = load_input_file('sample.txt')
    assert part1(inp1, 5) == 127

    inp = load_input_file('input.txt')
    assert part1(inp, 25) == 373803594


def part2(inp: List[int], preamble_length: int) -> int:
    weakness = part1(inp, preamble_length)
    for window_length in range(2, len(inp)):
        for i in range(len(inp) - window_length + 1):
            window = inp[i:i+window_length]
            if sum(window) == weakness:
                return min(window) + max(window)


def test_part2():
    print()
    inp1 = load_input_file('sample.txt')
    assert part2(inp1, 5) == 62

    inp = load_input_file('input.txt')
    assert part2(inp, 25) == 51152360
