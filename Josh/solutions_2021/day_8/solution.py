from collections import defaultdict
from dataclasses import dataclass, field
from os.path import dirname, join
from typing import Dict, List, Tuple

from solutions_2021 import get_filename

CURRENT_DIR = dirname(__file__)

DIGITS = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]


@dataclass
class Encoding:
    mapping: Dict[str, str] = field(default_factory=dict)

    def determine_mapping(self, codex: List[str]) -> None:
        freq = defaultdict(lambda: 0)  # type: ignore
        for segment in codex:
            for letter in segment:
                freq[letter] += 1

        sorted_freq = [k for k, v in sorted(freq.items(), key=lambda item: item[1])]

        self.mapping[sorted_freq[1]] = "b"
        self.mapping[sorted_freq[0]] = "e"
        self.mapping[sorted_freq[-1]] = "f"

        # We know 1 and 7, so, the difference between them is a
        segments = sorted(codex, key=len)
        self.mapping[list(set(segments[1]) - set(segments[0]))[0]] = "a"
        # 1 is obvs CF, so we need to determine which is C and which is F
        self.mapping[segments[0][0] if segments[0][1] == sorted_freq[-1] else segments[0][1]] = "c"

        is2d = sorted_freq[2] in segments[2]
        self.mapping[sorted_freq[2] if is2d else sorted_freq[3]] = "d"
        self.mapping[sorted_freq[2] if not is2d else sorted_freq[3]] = "g"

    def get_number(self, code: str) -> int:
        return DIGITS.index("".join(sorted(self.mapping[c] for c in code)))


def parse_input(file_name: str) -> List[Tuple[List[str], List[str]]]:
    with open(join(CURRENT_DIR, file_name), "r") as fp:
        contents = fp.read().split("\n")
    _output = []
    for i in range(len(contents)):
        notes, unique = contents[i].split(" | ")
        _output.append((notes.split(" "), unique.split(" ")))
    return _output


def part_two(file_name: str) -> int:
    puzzle_input = parse_input(file_name)
    total = 0
    for codex, ns in puzzle_input:
        encoder = Encoding()
        encoder.determine_mapping(codex)
        curr = 0
        for n in ns:
            curr = encoder.get_number(n) + curr * 10
        total += curr
    return total


if __name__ == "__main__":
    file = get_filename()

    result = part_two(file)
    print(f"Part two: {result=}")
