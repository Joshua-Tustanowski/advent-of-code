from typing import List, Tuple
import re
from functools import reduce


def parse_input(inp: str):
    section_blocks = inp.split('\n\n')
    assert len(section_blocks) == 3
    rules, your_ticket, other_tickets = section_blocks
    return rules, your_ticket, other_tickets


def part1(inp: List[str]) -> int:
    rules, your_ticket, other_tickets = parse_input(inp)
    # Get the rules
    rule_ranges = []
    for rule_line in rules.splitlines():
        s1, e1, s2, e2 = re.search(r'(\d+)-(\d+) or (\d+)-(\d+)', rule_line).groups()
        rule_ranges.append(range(int(s1), int(e1)+1))
        rule_ranges.append(range(int(s2), int(e2)+1))

    complete_value_range: set = reduce(lambda x, y: set(x) | set(y), rule_ranges)

    # Check all other tickets
    problematic_values = []
    for line in other_tickets.splitlines()[1:]:
        invalid_values = [int(i) for i in line.split(',') if int(i) not in complete_value_range]
        problematic_values.extend(invalid_values)
    return sum(problematic_values)


def load_input_file(filename: str):
    with open(filename, 'r') as inp:
        return inp.read()


def test_part1():
    inp1 = load_input_file('sample.txt')
    assert part1(inp1) == 71

    inp = load_input_file('input.txt')
    assert part1(inp) == 23036


def part2(inp: List[str]) -> int:
    rule_str, my_ticket, other_tickets = parse_input(inp)
    # Get the rules
    rules = {}
    for rule_line in rule_str.splitlines():
        field, s1, e1, s2, e2 = re.search(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', rule_line).groups()
        r1 = range(int(s1), int(e1)+1)
        r2 = range(int(s2), int(e2)+1)
        rules[field] = set(r1) | set(r2)

    complete_value_range: set = reduce(lambda x, y: set(x) | set(y), rules.values())

    # Weed out invalid tickets
    valid_lines = []
    for line in other_tickets.splitlines()[1:]:
        line = [int(i) for i in line.split(',')]
        if all(i in complete_value_range for i in line):
            valid_lines.append(line)

    # Determine the fields
    possible_field_matches = {}
    for col_n, col in enumerate(zip(*valid_lines)):
        possible_matches = []
        for field_name, field_range in rules.items():
            if all(c in field_range for c in col):
                possible_matches.append(field_name)
        possible_field_matches[col_n] = possible_matches
    """
      0: ['row']
      1: ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival station', 'arrival platform', 'arrival track', 'duration', 'route', 'row', 'train', 'type', 'wagon', 'zone']
      2: ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival track', 'route', 'row', 'train', 'wagon', 'zone']
      3: ['departure date', 'departure time', 'route', 'row', 'train', 'wagon', 'zone']
      4: ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival track', 'route', 'row', 'train', 'wagon', 'zone']
      5: ['row', 'wagon']
      6: ['route', 'row', 'wagon']
      7: ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival station', 'arrival track', 'duration', 'route', 'row', 'train', 'type', 'wagon', 'zone']
      8: ['departure location', 'departure station', 'departure platform', 'departure date', 'departure time', 'route', 'row', 'train', 'wagon', 'zone']
      9: ['route', 'row', 'train', 'wagon', 'zone']
     10: ['departure time', 'route', 'row', 'train', 'wagon', 'zone']
     11: ['route', 'row', 'train', 'wagon']
     12: ['departure location', 'departure platform', 'departure date', 'departure time', 'route', 'row', 'train', 'wagon', 'zone']
     13: ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'route', 'row', 'train', 'wagon', 'zone']
     14: ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival track', 'route', 'row', 'train', 'type', 'wagon', 'zone']
     15: ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival station', 'arrival platform', 'arrival track', 'class', 'duration', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon', 'zone']
     16: ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival track', 'duration', 'route', 'row', 'train', 'type', 'wagon', 'zone']
     17: ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival station', 'arrival platform', 'arrival track', 'duration', 'price', 'route', 'row', 'seat', 'train', 'type', 'wagon', 'zone']
     18: ['departure platform', 'departure date', 'departure time', 'route', 'row', 'train', 'wagon', 'zone']
     19: ['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time', 'arrival location', 'arrival station', 'arrival platform', 'arrival track', 'duration', 'route', 'row', 'seat', 'train', 'type', 'wagon', 'zone']
    """

    col_to_field_matches_list = sorted(possible_field_matches.items(), key=lambda x: len(x[1]))
    fields_done = set()
    field_locations = {}
    for col_n, possible_fields in col_to_field_matches_list:
        possible_fields = [f for f in possible_fields if f not in fields_done]
        assert len(possible_fields) == 1, f'Possible fields problem: {col_n}, {possible_fields}'
        field = possible_fields[0]
        field_locations[col_n] = field
        fields_done.add(field)

    # Calculate final answer
    my_ticket_values = [int(i) for i in my_ticket.splitlines()[1].split(',')]
    answer = 1
    for field, col_n in {v:k for k,v in field_locations.items()}.items():
        if field.startswith('departure'):
            answer *= my_ticket_values[col_n]
    return answer


def test_part2():
    inp = load_input_file('input.txt')
    assert part2(inp) == 1909224687553
