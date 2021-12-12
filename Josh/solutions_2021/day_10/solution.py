from os.path import dirname, join
from typing import List

from solutions_2021 import get_filename

CURRENT_DIR = dirname(__file__)

MAPPING_SCORE = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    "": 0,
}
BRACKET_MAPPING = {
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">",
}


COMPETITON_SCORING = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def parse_input(file_name: str) -> List[List[str]]:
    with open(join(CURRENT_DIR, file_name), "r") as fp:
        contents = fp.read().split("\n")
    return [[v for v in c] for c in contents]


def _is_corrupt(line: List[str]) -> str:
    stack = []
    for br in line:
        if br in ("(", "{", "[", "<"):
            stack.append(br)
        elif len(stack):
            value = stack.pop()
            if not BRACKET_MAPPING[value] == br:
                return br
    return ""


def _find_missing_ending(line: List[str]) -> str:
    stack = []
    for br in line:
        if br in ("(", "{", "[", "<"):
            stack.append(br)
        elif len(stack):
            stack.pop()
    values = []
    while stack:
        values.append(BRACKET_MAPPING[stack.pop()])
    return "".join(values)


def _competition_scoring(line: str) -> int:
    count = 0
    for char in line:
        score = COMPETITON_SCORING.get(char)
        assert score, f"Invalid score {char}"
        count = count * 5 + score
    return count


def part_one(lines: List[List[str]]) -> int:
    corrupt_chars = [_is_corrupt(line) for line in lines]
    return sum(MAPPING_SCORE.get(val) for val in corrupt_chars)  # type: ignore


def part_two(lines: List[List[str]]) -> int:
    valid_lines = [line for line in lines if not _is_corrupt(line)]
    projected_endings = [_find_missing_ending(line) for line in valid_lines]
    scores = sorted([_competition_scoring(line) for line in projected_endings])
    return scores[len(scores) // 2]


if __name__ == "__main__":
    file = get_filename()
    values = parse_input(file)

    result = part_one(values)
    print(f"Part one: {result=}")

    result = part_two(values)
    print(f"Part two: {result=}")
