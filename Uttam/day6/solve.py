from typing import List, Tuple
import re
from functools import reduce


def load_input_file(filename: str, lines: bool = True):
    with open(filename, 'r') as inp:
        return inp.read().split('\n\n') if lines else inp.read()


def find_number_of_questions_asked(inp: List[str], anyone: bool) -> int:
    # anyone = True: find number of questions that ANYONE answered yes to
    # anyone = False: find number of questions that EVERYONE answered yes to
    func = set.union if anyone else set.intersection
    no_of_questions_answered_yes = 0
    for group in inp:
        questions = reduce(func, [set(gl) for gl in group.splitlines()])
        no_of_questions_answered_yes += len(questions)
    return no_of_questions_answered_yes


def part1(inp: List[str]) -> int:
    return find_number_of_questions_asked(inp, True)


def test_part1():
    inp1 = load_input_file('sample.txt')
    assert part1(inp1) == 11

    inp = load_input_file('input.txt')
    assert part1(inp) == 6504


def part2(inp: List[str]) -> int:
    return find_number_of_questions_asked(inp, False)


def test_part2():
    inp1 = load_input_file('sample.txt')
    assert part2(inp1) == 6

    inp = load_input_file('input.txt', lines=True)
    assert part2(inp) == 3351
