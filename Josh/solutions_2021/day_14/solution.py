import copy
from collections import defaultdict
from math import ceil
from os.path import dirname, join
from typing import Dict, Tuple
from collections import Counter

from solutions_2021 import get_filename

CURRENT_DIR = dirname(__file__)


def parse_input(file_name: str) -> Tuple[str, Dict[str, str]]:
    with open(join(CURRENT_DIR, file_name), "r") as fp:
        template, mappings = fp.read().split('\n\n')
    rules = {}
    for mapping in mappings.split('\n'):
        start, end = mapping.split(' -> ')
        rules[start] = end
    return template, rules


def part_one(template: str, rules: Dict[str, str], steps: int = 10) -> int:
    res = _get_counter(template, rules, steps)
    _max, _min = _get_extreme_values_from_dict(res)
    return _max - _min


def _get_extreme_values_from_dict(v: Dict[str, int]) -> Tuple[int, int]:
    largest, smallest = max(v, key=v.get), min(v, key=v.get)
    return v[largest], v[smallest]


def _get_counter(template: str, rules: Dict[str, str], steps: int = 10) -> Dict[str, int]:
    curr = template
    # print(f"Template:\t  {template}")
    for i in range(1, steps + 1):
        # start = time.time()
        values = [f"{curr[i]}{rules[curr[i:i+2]]}" for i in range(len(curr) - 1)]
        curr = "".join([*values, curr[len(curr)-1]])
        # print(f"Step {i} took: {time.time() - start}")
        # print(f"After step {i}: {curr}")
    return Counter(curr)


def part_two(template: str, rules: Dict[str, str], steps: int = 5):
    pairs = defaultdict(int)
    for i in range(len(template) - 1):
        pairs[template[i:i+2]] += 1

    for step in range(0, steps):
        inserts = copy.deepcopy(pairs)
        for pair in inserts:
            count = inserts[pair]

            pairs[pair[0] + rules[pair]] += count
            pairs[rules[pair] + pair[1]] += count
            pairs[pair] -= count

    result = defaultdict(int)
    for key in pairs.keys():
        result[key[0]] += pairs[key] / 2
        result[key[1]] += pairs[key] / 2
    _max, _min = _get_extreme_values_from_dict(result)
    return int(ceil(_max - _min))


if __name__ == "__main__":
    file = get_filename()
    initial, polymer_rules = parse_input(file)

    result = part_one(initial, polymer_rules, steps=10)
    print(f"Part one: {result=}")
    result = part_two(initial, polymer_rules, steps=40)
    print(f"Part two: {result=}")
