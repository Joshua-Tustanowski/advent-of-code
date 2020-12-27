from collections import deque


def part_one(player_1, player_2):
    while len(player_1) and len(player_2):
        card_1, card_2 = player_1.pop(0), player_2.pop(0)
        cards_1, cards_2 = _round(card_1, card_2)
        player_1.extend(cards_1)
        player_2.extend(cards_2)
    return player_1 if player_1 else player_2


def part_two(player_1, player_2):
    memoisation = set()

    def helper(deck_1, deck_2, game):
        eins, zwei = map(deque, (deck_1, deck_2))
        rounds = 1
        while eins and zwei:
            if hash((tuple(eins), tuple(zwei), game)) in memoisation:
                return 1, eins
            else:
                memoisation.add(hash((tuple(eins), tuple(zwei), game)))
            card_1, card_2 = eins.popleft(), zwei.popleft()
            if len(eins) >= card_1 and len(zwei) >= card_2:
                winner, _ = helper(list(eins)[:card_1], list(zwei)[:card_2], game + 1)
            elif card_1 > card_2:
                winner = 1
            else:
                winner = 2

            if winner == 1:
                eins.extend([card_1, card_2])
            else:
                zwei.extend([card_2, card_1])
            rounds += 1
        return 1 if eins else 2, eins if eins else zwei

    return helper(player_1, player_2, game=1)[1]


def _round(card_1, card_2):
    if card_1 > card_2:
        return [card_1, card_2], []
    return [], [card_2, card_1]


def load(file_name):
    players = open(file_name).read().split("\n\n")
    player_1, player_2 = players
    return _format(player_1), _format(player_2)


def _format(player):
    players = player.replace("\n", " ")
    _, players = players.split(": ")
    return [int(player) for player in players.split(" ")]


def score(array):
    return sum([(len(array) - i) * val for i, val in enumerate(array)])


if __name__ == "__main__":
    player_1, player_2 = load("input.txt")
    print(score(part_one(player_1, player_2)))
    player_1, player_2 = load("input.txt")
    print(score(part_two(player_1, player_2)))
