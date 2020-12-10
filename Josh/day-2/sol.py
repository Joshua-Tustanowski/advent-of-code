with open('input.txt', 'r') as file:
    input_ = file.read().split("\n")
    valid = 0
    for entry in input_:
        if len(entry):
            range_, letter_, string_ = entry.split(" ")
            range_ = range_.split("-")
            min_, max_ = int(range_[0]), int(range_[-1])
            letter_ = letter_[:-1]
            count_ = 0
            if string_[min_-1] == letter_:
                count_ += 1
            if string_[max_-1] == letter_:
                count_ += 1
            if count_ == 1:
                valid +=1
    print(valid)
