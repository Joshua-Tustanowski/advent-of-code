from collections import Counter
from typing import List


def play_game(inp: List[int], turns: int) -> int:
    counter = len(inp)
    history = inp
    # print(f'Starting nums: {inp}')
    counts = Counter(history)
    last_seen_at_idx = {v: n for n, v in enumerate(inp, 1)}
    last_number = history[-1]
    while counter < turns:
        counter += 1
        # print(f'\n----\nTurn {counter}')
        # last_number = history[-1]
        # print(f'Last number: {last_number}')
        if counts[last_number] == 1:
            # print(f'{last_number} has only occurred once yet, so the next number will be 0')
            next_number = 0
        else:
            # print(f'Where did {last_number} last occur')
            # print(f'History: {history}')
            # print(f'Finding where {last_number} appears in {last_seen_at_idx}')
            prev_occurrence_turn = last_seen_at_idx[last_number]
            # print(f'{last_number} last occurred at turn {prev_occurrence_turn}')
            next_number = counter - 1 - prev_occurrence_turn
            # print(f'Next number is therefore {counter - 1} - {prev_occurrence_turn} = {next_number}')
            # last_seen_idxs[next_number] = counter
        history.append(next_number)
        counts[next_number] += 1
        # print(f'Last seen dict: {last_seen_at_idx}')
        # print(f'Updating last seen index for {last_number} to turn {counter-1}')
        last_seen_at_idx[last_number] = counter - 1
        # last_seen_at_idx[last_number] = counter
        # counter += 1
        last_number = next_number
    return next_number


def part1(inp: List[int]) -> int:
    return play_game(inp, 2020)


def load_input_file(filename: str, lines: bool = True):
    with open(filename, "r") as inp:
        return inp.readlines() if lines else inp.read()


def test_part1():
    # print()
    assert part1([0, 3, 6]) == 436
    assert part1([1, 3, 2]) == 1
    assert part1([2, 1, 3]) == 10
    assert part1([1, 2, 3]) == 27
    assert part1([2, 3, 1]) == 78
    assert part1([3, 2, 1]) == 438
    assert part1([3, 1, 2]) == 1836

    assert part1([6, 4, 12, 1, 20, 0, 16]) == 475


def part2(inp: List[int]) -> int:
    return play_game(inp, 30_000_000)


def test_part2():
    assert part2([0, 3, 6]) == 175594
    assert part2([1, 3, 2]) == 2578
    assert part2([2, 1, 3]) == 3544142
    assert part2([1, 2, 3]) == 261214
    assert part2([2, 3, 1]) == 6895259
    assert part2([3, 2, 1]) == 18
    assert part2([3, 1, 2]) == 362

    assert part2([6, 4, 12, 1, 20, 0, 16]) == 11261
