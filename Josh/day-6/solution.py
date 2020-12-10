def get_customs_sum(custom):
    count = {}
    for char in custom:
        if char not in count:
            count[char] = 1
    return len(count)

def solution(file):
    with open(file, 'r') as file:
        input_data = file.read().split("\n\n")
        sum_ = 0
        for input_ in input_data:
            sum_ += get_everyone_sum(input_)
        print(sum_)

def get_everyone_sum(input_data):
    input_data = input_data.replace('\n', ' ')
    input_data = input_data.split(' ')
    count = {}
    for person in input_data:
        for char in person:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
    matching = 0
    for char, counter in count.items():
        if counter == len(input_data):
            matching += 1
    return matching

if __name__ == "__main__":
    solution('input.txt')
