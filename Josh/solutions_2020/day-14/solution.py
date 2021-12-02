import re


def read_and_parse_file(filename: str):
    with open(filename, "r") as fp:
        cnts = fp.read().splitlines()
    mask_rgx = re.compile(r"(mask)\s=\s([10X]+)")
    mem_rgx = re.compile(r"^mem\[(\d+)\]\s=\s(\d+)")
    results = {}
    for res in cnts:
        if res[:4] == "mask":
            mask = mask_rgx.match(res)
            bitmask = mask.group(2)
            results[bitmask] = []
        if mask is not None:
            bits = mem_rgx.match(res)
            if bits is not None:
                results[bitmask].append((bits.group(1), bits.group(2)))
    return results


def b2d(bin: str):
    res = 0
    i = len(bin) - 1
    for val in bin:
        res += int(val) * 2 ** (i)
        i -= 1
    return res


if __name__ == "__main__":
    results = read_and_parse_file("input.txt")
    values = {}
    # print(results)
    for mask, addresses in results.items():
        # print(mask)
        for address in addresses:
            _address, value = address
            binary = bin(int(value))[2:]
            binary = f"{(36-len(binary)) * '0'}{binary}"
            binary = [char for char in binary]
            for i in range(len(binary)):
                if mask[i] != "X":
                    binary[i] = mask[i]
            # print("".join(binary))
            values[int(_address)] = b2d(binary)
    print(sum(values.values()))
