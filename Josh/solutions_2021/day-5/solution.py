from __future__ import annotations

import re

from math import ceil, log10

from dataclasses import dataclass
from typing import List, Tuple
from os.path import dirname, join

from solutions_2021 import get_filename

CURRENT_DIR = dirname(__file__)

WIDTH = 10
HEIGHT = 10


def _get_min_max(a, b):
    return max(a, b), min(a, b)


def round_to_base10(a: int) -> int:
    return 10 ** ceil(log10(a))


def _infer_width_height(
    coordinates: List[Tuple[Location, Location]]
) -> Tuple[int, int]:
    width, height = 0, 0
    for start, end in coordinates:
        max_x = max(start.x, end.x)
        max_y = max(start.y, end.y)
        width = max(width, round_to_base10(max_x))
        height = max(height, round_to_base10(max_y))

    max_var = max(width, height)
    return max_var, max_var


@dataclass
class Location:
    x: int
    y: int
    counter: int = 0

    def get_line_coordinates(self, other: Location) -> List[Location]:
        if self.x == other.x:
            max_val, min_val = _get_min_max(self.y, other.y)
            return [Location(x=self.x, y=val) for val in range(min_val, max_val + 1)]
        elif self.y == other.y:
            max_val, min_val = _get_min_max(self.x, other.x)
            return [Location(x=val, y=self.y) for val in range(min_val, max_val + 1)]
        else:
            if self > other:
                start, end = other, self
            else:
                start, end = self, other

            if start.y < end.y:
                return [
                    Location(x=start.x + i, y=start.y + i)
                    for i in range((end.x - start.x) + 1)
                ]
            else:
                return [
                    Location(x=start.x + i, y=start.y - i)
                    for i in range((end.x - start.x) + 1)
                ]

    def __gt__(self, other):
        return self.x > other.x

    def __str__(self):
        symbol = "." if self.counter == 0 else self.counter
        return f"{symbol}"


@dataclass
class OceanFloor:
    tiles: List[List[Location]]

    def update(self, loc: Location) -> None:
        self.tiles[loc.x][loc.y].counter += 1

    def print(self):
        for row in self.tiles:
            row = " ".join([str(col) for col in row])
            print(row)

    def count_intersections(self):
        intersections = 0
        for row in self.tiles:
            for col in row:
                if col.counter >= 2:
                    intersections += 1
        return intersections


def parse_input(filename: str) -> List[Tuple[Location, Location]]:
    with open(join(CURRENT_DIR, filename), "r") as fp:
        contents = fp.read().split("\n")
    locations = []
    pattern = re.compile(r"(\d+,\d+)\s->\s(\d+,\d+)")
    for content in contents:
        match = re.match(pattern, content)
        start = [int(v) for v in match.group(1).split(",")]
        end = [int(v) for v in match.group(2).split(",")]
        locations.append((Location(*start), Location(*end)))
    return locations


def solution(filename: str) -> int:
    locations = parse_input(filename)
    width, height = _infer_width_height(locations)

    floor = OceanFloor(
        tiles=[[Location(x=x, y=y) for y in range(width)] for x in range(height)]
    )
    for start, end in locations:
        line_coordinates = start.get_line_coordinates(end)
        if not line_coordinates:
            continue
        for coordinate in line_coordinates:
            floor.update(coordinate)
    # floor.print()
    return floor.count_intersections()


if __name__ == "__main__":
    file = get_filename()

    result = solution(file)
    print(f"Solution: {result=}")
