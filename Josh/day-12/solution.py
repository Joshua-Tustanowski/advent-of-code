import re

directions = {
    'E': (+1, 0),
    'W': (-1, 0),
    'N': (0, +1),
    'S': (0, -1),
}


def read_and_parse_input(filename: str):
    with open(filename, 'r') as fp:
        res = fp.read()
        contents = res.split('\n')
    regex = re.compile(r'([A-Z])(\d+)')
    output = []
    for action in contents:
        match = regex.match(action)
        output.append((match.group(1), int(match.group(2))))
    return output


def handle_turn(direction, action, value):
    directions = {(0,1): 'N', (1,0): 'E', (0,-1): 'S', (-1, 0): 'W'}
    direction_strs = ['N', 'E', 'S', 'W']
    direction_str = directions[direction]
    idx = direction_strs.index(direction_str)
    counter = value // 90
    if action == 'R':
        for i in range(counter):
            idx = (idx + 1) % 4
    if action == 'L':
        for i in range(counter):
            idx = (idx - 1) % 4
    for _direction, direction_str in directions.items():
        if direction_str == direction_strs[idx]:
            return _direction


def manhattan_dist(position):
    x, y = position
    return abs(x) + abs(y)


def part_one(actions):
    direction = (1, 0)
    position = (0, 0)
    for action, value in actions:
        x, y = position
        if action == 'R' or action == 'L':
            direction = handle_turn(direction, action, value)
        elif action == 'N':
            y = y + value
        elif action == 'S':
            y = y - value
        elif action == 'E':
            x = x + value
        elif action == 'W':
            x = x - value
        elif action == 'F':
            x = x + value * direction[0]
            y = y + value * direction[1]
        position = (x, y)
    return manhattan_dist(position)


def right_rotation(position: (int, int), degree: int) -> (int, int):
    x, y = position
    if degree % 360 == 0:
        return x, y
    elif degree % 360 == 90:
        return y, -x
    elif degree % 360 == 180:
        return -x, -y
    elif degree % 360 == 270:
        return -y, x


def left_rotation(position: (int, int), degree: int) -> (int, int):
    return right_rotation(position, 360 - degree)


def part_two(actions):
    coord = (0, 0)
    waypoint = (+10, +1)

    for action, value in actions:
        if action == 'F':
            coord = (
                coord[0] + waypoint[0] * value,
                coord[1] + waypoint[1] * value,
            )
        elif action in directions.keys():
            waypoint = (
                waypoint[0] + directions[action][0] * value,
                waypoint[1] + directions[action][1] * value,
            )
        elif action == 'L':
            waypoint = left_rotation(waypoint, value)
        elif action == 'R':
            waypoint = right_rotation(waypoint, value)

    return manhattan_dist(coord)


if __name__ == "__main__":
    actions = read_and_parse_input('input.txt')
    print(part_one(actions))
    print(part_two(actions))