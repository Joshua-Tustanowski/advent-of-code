def read_and_parse_input(file_name: str) -> list:
    with open(file_name, 'r') as _input:
        _input = _input.read()
        _input = _input.split('\n')
    try:
        for i in range(len(_input)):
            _input[i] = int(_input[i])
    except Exception as ex:
        print(ex)
    return _input

if __name__ == "__main__":
    print(read_and_parse_input('test.txt'))
