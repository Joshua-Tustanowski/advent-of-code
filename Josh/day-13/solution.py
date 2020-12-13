from typing import List, Tuple


def read_and_parse_input(filename: str) -> List[Tuple[str, str]]:
    with open(filename, 'r') as fp:
        timestamp, tmp_ids = fp.read().splitlines()
    bus_ids = []
    for val in tmp_ids.split(','):
        if val == 'x':
            bus_ids.append(-1)
        else:
            bus_ids.append(int(val))
    return int(timestamp), bus_ids


def part_one(data: Tuple[int, List[int]]) -> int:
    timetamp, ids = data
    earliest_time, earliest_id = float('inf'), None
    for id in ids:
        if id < 0:
            continue
        depart_time = timetamp + id - (timetamp % id)
        if depart_time < earliest_time:
            earliest_time = depart_time
            earliest_id = id
    return (earliest_time - timetamp) * earliest_id


if __name__ == "__main__":
    content = read_and_parse_input('input.txt')
    print(part_one(content))
