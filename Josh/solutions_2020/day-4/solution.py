def process_input_file_to_dicts(file):
    with open(file) as test:
        input_ = test.read()
    credentials = []
    input_ = input_.split("\n\n")
    for credential in input_:
        credential = credential.replace("\n", " ")
        split_credentials = credential.split(" ")
        personal_credential = {}
        for split in split_credentials:
            key, value = split.split(":")
            personal_credential[key] = value
        credentials.append(personal_credential)
    return credentials


def validate_key(credentials, key):
    if key == "byr" and len(credentials[key]) == 4 and 1920 <= int(credentials[key]) <= 2002:
        return True
    if key == "iyr" and len(credentials[key]) == 4 and 2010 <= int(credentials[key]) <= 2020:
        return True
    if key == "eyr" and len(credentials[key]) == 4 and 2020 <= int(credentials[key]) <= 2030:
        return True
    if key == "hgt":
        num_part = ""
        measure_part = ""
        for char in credentials[key]:
            if char.isdigit():
                num_part += char
            elif char.isalpha():
                measure_part += char
        height = int(num_part)
        if measure_part == "cm" and not 150 <= height <= 193:
            return False
        if measure_part == "in" and not 59 <= height <= 76:
            return False
        if measure_part != "cm" and measure_part != "in":
            return False
        return True
    if key == "hcl" and credentials[key][0] == "#" and len(credentials[key][1:]) == 6:
        for i in range(1, len(credentials[key])):
            if credentials[key][i].isdigit():
                continue
            elif credentials[key][i].isalpha():
                char = ord(credentials[key][i]) - 97
                if not (0 <= char <= 5):
                    return False
            else:
                return False
        return True
    if key == "ecl" and credentials[key] in [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    ]:
        return True
    if key == "pid" and len(credentials[key]) == 9:
        return True
    if key == "cid":
        return True
    return False


def check_valid(credentials, expected, optional):
    expected = {key: False for key in expected if key not in optional}
    count = 0
    for key in credentials.keys():
        if key in expected and expected[key] == False and validate_key(credentials, key):
            expected[key] = True
            count += 1
    return count == len(expected)


def main(file):
    passports = process_input_file_to_dicts(file)
    expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    count = 0
    for passport in passports:
        print(passport, check_valid(passport, expected_fields, optional=["cid"]))
        if check_valid(passport, expected_fields, optional=["cid"]):
            count += 1
    print(count)


if __name__ == "__main__":
    main("input.txt")
