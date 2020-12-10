def get_graph(file):
    """ convert the input text file into a 2d array """
    count = len(open(file).readlines())
    array = []
    with open(file, 'r') as input_file:
        for line in range(count):
            line = input_file.readline()
            array.append([char for char in line[:-1]])
    return array

def get_count(file):
    graph = get_graph(file)
    curr = [0, 0]
    max_right = len(graph[0])
    max_down = len(graph)
    count = 0
    while curr[0] < max_down and curr[1] < max_right:
        if graph[curr[0]][curr[1]] == '#' or graph[curr[0]][curr[1]] == 'X':
            count += 1
        print(curr, graph[curr[0]][curr[1]])
        curr[0] += 3
        curr[1] += 1
    print(count)

with open('input.txt', 'r') as input_file: input_map = [[field == '#' for field in line] for line in input_file.read().split('\n')]; print(str([line[(pos * 3) % len(line)] for pos, line in enumerate(input_map)].count(True)) + '\n' + str(eval('*'.join([str(i) for i in [[line[(pos * slope[0]) % len(line)] for pos, line in enumerate([n for c, n in enumerate(input_map) if c % slope[1] == 0])].count(True) for slope in [[1,1], [3, 1], [5, 1], [7,1], [1,2]]]]))))
