from typing import List, Tuple
import re
from collections import Counter
import logging

DEBUG = 0
if DEBUG:
    logging.getLogger().setLevel(logging.DEBUG)


def play_game(inp: List[int], turns: int) -> int:
    counter = len(inp)
    history = inp
    logging.debug(f'Starting nums: {inp}')
    counts = Counter(history)
    while counter < turns:
        counter += 1
        logging.debug(f'\n----\nTurn {counter}')
        last_number = history[-1]
        logging.debug(f'Last number: {last_number}')
        if counts[last_number] == 1:
            logging.debug(f'{last_number} has only occurred once yet, so the next number will be 0')
            next_number = 0
        else:
            logging.debug(f'Where did {last_number} last occur')
            logging.debug(f'History: {history}')
            logging.debug(f'Finding where {last_number} appears in {history[-2::-1]}')
            prev_occurrence_turn = len(history) - history[-2::-1].index(last_number) - 1
            logging.debug(f'{last_number} last occurred at turn {prev_occurrence_turn}')
            next_number = counter - 1 - prev_occurrence_turn
            logging.debug(f'Next number is therefore {counter - 1} - {prev_occurrence_turn} = {next_number}')
        history.append(next_number)
        counts[next_number] += 1
    return next_number


def part1(inp: List[int]) -> int:
    return play_game(inp, 2020)


def load_input_file(filename: str, lines: bool = True):
    with open(filename, 'r') as inp:
        return inp.readlines() if lines else inp.read()


def test_part1():
    assert part1([0, 3, 6]) == 436
    assert part1([1, 3, 2]) == 1
    assert part1([2, 1, 3]) == 10
    assert part1([1, 2, 3]) == 27
    assert part1([2, 3, 1]) == 78
    assert part1([3, 2, 1]) == 438
    assert part1([3, 1, 2]) == 1836

    assert part1([6, 4, 12, 1, 20, 0, 16]) == 475


def part2(inp: List[int]) -> int:
    # todo - too long, won't work
    return play_game(inp, 30_000_000)


# def test_part2():
#     assert part2([0, 3, 6]) == 175594
#     assert part2([1, 3, 2]) == 2578
#     assert part2([2, 1, 3]) == 3544142
#     assert part2([1, 2, 3]) == 261214
#     assert part2([2, 3, 1]) == 6895259
#     assert part2([3, 2, 1]) == 18
#     assert part2([3, 1, 2]) == 362
#
#     assert part2([6, 4, 12, 1, 20, 0, 16]) == None
