from dataclasses import dataclass
from enum import auto, Enum
import re
from os.path import dirname, join
from typing import List, Tuple

from solutions_2021 import DEBUG

CURRENT_DIR = dirname(__file__)


class Direction(Enum):
    FORWARD = auto()
    DOWN = auto()
    UP = auto()


@dataclass
class Location:
    x: int = 0
    y: int = 0

    def move(self, direction: Direction, distance: int):
        if direction == Direction.FORWARD:
            self.x += distance
        elif direction == Direction.DOWN:
            self.y += distance
        elif direction == Direction.UP:
            self.y -= distance
        else:
            raise ValueError(f"Direction {direction} not a valid direction")


@dataclass
class LocationAim(Location):
    aim: int = 0

    def move(self, direction: Direction, distance: int):
        if direction == Direction.FORWARD:
            self.x += distance
            self.y += self.aim * distance
        elif direction == Direction.DOWN:
            self.aim += distance
        elif direction == Direction.UP:
            self.aim -= distance
        else:
            raise ValueError(f"Direction {direction} not a valid direction")


mapping = {
    "forward": Direction.FORWARD,
    "down": Direction.DOWN,
    "up": Direction.UP,
}

pattern = re.compile(r"([a-z]+)\s(\d+)")


def parse_file(file_name: str) -> List[Tuple[Direction, int]]:
    with open(join(CURRENT_DIR, file_name), "r") as fp:
        contents = fp.read().split("\n")
    instructions = []
    for instruction in contents:
        matched = pattern.match(instruction)
        direction = mapping.get(matched.group(1))
        assert direction, f"no direction for instruction {instruction}"
        instructions.append((direction, int(matched.group(2))))
    return instructions


def part_one(file_name: str) -> int:
    instructions = parse_file(file_name)
    loc = Location()
    for instruction in instructions:
        direction, distance = instruction
        loc.move(direction, distance)
    return loc.x * loc.y


def part_two(file_name: str) -> int:
    instructions = parse_file(file_name)
    loc = LocationAim()
    for instruction in instructions:
        direction, distance = instruction
        loc.move(direction, distance)
    return loc.x * loc.y


if __name__ == "__main__":
    file = "basic-input.txt" if not DEBUG else "sample-input.txt"

    result = part_one(file)
    print(f"Part one: {result=}")

    result = part_two(file)
    print(f"Part one: {result=}")
