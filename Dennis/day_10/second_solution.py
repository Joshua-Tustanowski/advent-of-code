from pathlib import Path
from collections import Counter

file = Path('input/data2.txt')

data = sorted([0] + [int(line) for line in file.open('r')])

counter = Counter({0: 1})

for x in data:
    counter[x+1] += counter[x]
    counter[x+2] += counter[x]
    counter[x+3] += counter[x]

print(counter[max(data) + 3])  # ans: 1727094849536
