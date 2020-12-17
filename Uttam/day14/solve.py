from typing import List, Tuple
import re
from itertools import product


def parse_sections(blob: List[str]) -> List[dict]:
    sections = []
    no_of_lines = len(blob)
    for n, line in enumerate(blob):
        if n == no_of_lines - 1:
            sections.append(section)
        if 'mask' in line:
            if n != 0:
                sections.append(section)
            section = {'mask': re.search('(?<=mask = )[X01]{36}', line).group(), 'updates': []}
        else:
            values = re.search('mem\[(\d+)\] = (\d+)', line).groups()
            k, v = int(values[0]), int(values[1])
            section['updates'].append((k, v))
    return sections


def apply_mask(number: int, mask: str) -> int:
    number_in_binary = list("{0:b}".format(number).zfill(36))
    for n, m in enumerate(mask):
        assert m in ('X01')
        if m == 'X':
            continue
        else:
            number_in_binary[n] = m
    return int(''.join(number_in_binary), base=2)


def part1(inp: List[str]) -> int:
    sections = parse_sections(inp)
    memory = {}
    for section in sections:
        mask = section['mask']
        for k, v in section['updates']:
            number_after_mask = apply_mask(v, mask)
            memory[k] = number_after_mask
    return sum(memory.values())


def load_input_file(filename: str, lines: bool = True):
    with open(filename, 'r') as inp:
        return inp.readlines() if lines else inp.read()


def test_part1():
    inp1 = load_input_file('sample.txt')
    assert part1(inp1) == 165

    inp = load_input_file('input.txt')
    assert part1(inp) == 3059488894985


def apply_mask2(original_address: int, mask: str) -> List[int]:
    original_address_in_binary = list("{0:b}".format(original_address).zfill(36))
    addresses: List[int] = []
    no_of_floating_bits = 0
    for n, m in enumerate(mask):
        assert m in 'X01'
        if m == 'X':
            original_address_in_binary[n] = 'X'
            no_of_floating_bits += 1
        elif m == '0':
            continue
        elif m == '1':
            original_address_in_binary[n] = '1'
    result = ''.join(original_address_in_binary)

    # Go through the address permutations
    for bit_combination in product([0, 1], repeat=no_of_floating_bits):
        x_counter = 0
        address_chars = []
        for c in result:
            if c == 'X':
                address_chars.append(str(bit_combination[x_counter]))
                x_counter += 1
            else:
                address_chars.append(c)
        addresses.append(int(''.join(address_chars), base=2))
    return addresses


def part2(inp: List[str]) -> int:
    sections = parse_sections(inp)
    memory = {}
    for section in sections:
        mask = section['mask']
        for k, v in section['updates']:
            addresses = apply_mask2(k, mask)
            for address in addresses:
                memory[address] = v
    return sum(memory.values())


def test_part2():
    inp1 = load_input_file('sample_part2.txt')
    assert part2(inp1) == 208

    inp = load_input_file('input.txt')
    assert part2(inp) == 2900994392308
