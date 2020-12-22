from typing import List, Tuple
import re


def parse_starting_cards(inp: str) -> Tuple[List[int], List[int]]:
    p1_block, p2_block = inp.split('\n\n')
    p1_starting_cards = [int(i) for i in p1_block.splitlines()[1:]]
    p2_starting_cards = [int(i) for i in p2_block.splitlines()[1:]]
    return p1_starting_cards, p2_starting_cards


def part1(inp: str) -> int:
    p1_cards, p2_cards = parse_starting_cards(inp)
    counter = 1
    while True:
        if len(p1_cards) == 0 or len(p2_cards) == 0:  # end of game
            break

        print(f'\n-- Round {counter} --')
        print("Player 1's deck: {}".format(', '.join(str(i) for i in p1_cards)))
        print("Player 2's deck: {}".format(', '.join(str(i) for i in p2_cards)))
        p1_plays, p2_plays = p1_cards[0], p2_cards[0]
        print(f'Player 1 plays: {p1_plays}')
        print(f'Player 2 plays: {p2_plays}')
        assert p1_plays != p2_plays, f'Cards should not be equal: {p1_plays}, {p2_plays}'
        if p1_plays > p2_plays:
            print('Player 1 wins the round!')
            p1_cards = p1_cards[1:] + [p1_plays, p2_plays]
            p2_cards = p2_cards[1:]
        else:
            print('Player 2 wins the round!')
            p2_cards = p2_cards[1:] + [p2_plays, p1_plays]
            p1_cards = p1_cards[1:]
        counter += 1

    # Calculate final score
    winners_stack = p1_cards + p2_cards
    return sum(n * i for n, i in enumerate(reversed(winners_stack), 1))


def load_input_file(filename: str):
    with open(filename, 'r') as inp:
        return inp.read()


def test_part1():
    inp1 = load_input_file('sample.txt')
    assert part1(inp1) == 306

    inp = load_input_file('input.txt')
    assert part1(inp) == 32783


def part2(inp: List[str]) -> int:
    pass


# def test_part2():
    # inp1 = load_input_file('sample.txt')
    # assert part2(inp1) == None

    # inp = load_input_file('input.txt')
    # assert part2(inp) == None
