from pathlib import Path

with Path('input/6b').open('r') as file:
    content = file.read()

data = content.split('\n\n')

data_2 = [collection.split('\n') for collection in data]

print(data)

commonality = 0
for group in data_2:
    score = len(set(group[0]))
    if len(group) > 1:
        questions = set(group[0])
        commons = score
        for person in group[1:]:
            person = set(person)
            questions = questions.intersection(person)
            commons = len(questions)
        score = commons
    commonality += score

print(commonality)
