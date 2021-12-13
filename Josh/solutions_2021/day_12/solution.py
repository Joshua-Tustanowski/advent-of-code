from collections import defaultdict
from dataclasses import dataclass
from os.path import dirname, join
from typing import Dict, List

from solutions_2021 import get_filename

CURRENT_DIR = dirname(__file__)


def parse_input(file_name: str):
    with open(join(CURRENT_DIR, file_name), "r") as fp:
        contents = fp.read().split("\n")

    graph = defaultdict(list)
    for entry in contents:
        start, end = entry.split("-")
        graph[end].append(start)
        graph[start].append(end)
    return graph


def part_one(graph: Dict[str, List[str]]):
    def _search(current, path: List[str]):
        if current == "end":
            paths.append(tuple(path))
        for n in graph[current]:
            if (n == "start" or n.islower() and n in path) or (
                n == "start" or n.islower() and n in path and any(path.count(y) > 1 for y in path if y.islower())
            ):
                continue
            _search(n, path + [n])

    paths = []
    _search("start", ["start"])
    return len(paths)


def part_two(graph: Dict[str, List[str]]):
    def _search(current, path: List[str], visited: bool = False):
        if current == "end":
            paths.add(tuple(path))
            return
        for n in graph[current]:
            if (n == "start" or n.islower() and n in path and not visited) or (
                n == "start"
                or n.islower()
                and n in path
                and any(path.count(y) > 1 for y in path if y.islower())
                and visited
            ):
                continue
            _search(n, path + [n], visited)
        return len(paths)

    paths = set()
    _search("start", ["start"], visited=True)
    return len(paths)


if __name__ == "__main__":
    file = get_filename()

    values = parse_input(file)
    result = part_one(values)

    print(f"Part one: {result}")
    result = part_two(values)
    print(f"Part two: {result}")
