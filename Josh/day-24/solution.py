# Guide on hexagonal coordinates: https://www.redblobgames.com/grids/hexagons/
def move(coords, d):
    x, y, z = coords
    assert x + y + z == 0 and d in ["e", "w", "se", "sw", "ne", "nw"]
    if d == "e":
        return x + 1, y - 1, z
    if d == "w":
        return x - 1, y + 1, z
    if d == "ne":
        return x + 1, y, z - 1
    if d == "nw":
        return x, y + 1, z - 1
    if d == "se":
        return x, y - 1, z + 1
    if d == "sw":
        return x - 1, y, z + 1


def get_neighbours(coord):
    return [move(coord, dir) for dir in ["e", "w", "se", "sw", "ne", "nw"]]


if __name__ == "__main__":
    strings = open("input.txt").read().split("\n")
    black = {}
    for string in strings:
        i = 0
        position = (0, 0, 0)
        while i < len(string):
            if string[i] == "s" or string[i] == "n":
                direction = string[i : i + 2]
                i += 2
            else:
                direction = string[i]
                i += 1
            position = move(position, direction)
        is_flipped = black.get(position, False)
        black[position] = not is_flipped
    print(sum(v for v in black.values() if v))
    # part 2
    for _ in range(100):
        for coord in list(black):
            neighbours = get_neighbours(coord)
            for neighbour in neighbours:
                if neighbour not in black:
                    black[neighbour] = False

        new_tiles = {}
        for coord, is_flipped in black.items():
            flip_count = len(
                [
                    neighbour
                    for neighbour in get_neighbours(coord)
                    if black.get(neighbour, False)
                ]
            )
            if is_flipped and (flip_count == 0 or flip_count > 2):
                is_flipped = False
            elif not is_flipped and flip_count == 2:
                is_flipped = True
            new_tiles[coord] = is_flipped
        black = new_tiles
    print(sum(v for v in black.values() if v))
