from typing import List
import copy


def read_and_parse_input(file_name: str):
    with open(file_name, 'r') as input_file:
        contents = input_file.readlines()
    for i, content in enumerate(contents):
        content = content.replace('\n', '')
        contents[i] = [char for char in content]
    return contents


def process_point(i: int, j: int, value: str, graph) -> str:
    count = 0
    adjacent = [(1,0), (0,1), (1,1), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1)]
    if value == 'L':
        tmp_cntr = 0
        for neighbour in adjacent:
            x_off, y_off = neighbour
            if 0 <= x_off + i < len(graph) and 0 <= y_off + j < len(graph[i]):
                if graph[x_off+i][y_off+j] != '#':
                    count += 1
            else:
                tmp_cntr += 1
        return count == len(adjacent) - tmp_cntr
    elif value == '#':
        for neighbour in adjacent:
            x_off, y_off = neighbour
            if 0 <= x_off + i < len(graph) and 0 <= y_off + j < len(graph[j]):
                if graph[x_off+i][y_off+j] == '#':
                    count += 1
        return count >= 4


def fill_seats(graph: List[List[str]]) -> List[List[str]]:
    output = copy.deepcopy(graph)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 'L':
                count = process_point(i, j, graph[i][j], graph)
                output[i][j] = '#' if count else graph[i][j]
            elif graph[i][j] == '#':
                count = process_point(i, j, graph[i][j], graph)
                output[i][j] = 'L' if count else graph[i][j]
            else:
                output[i][j] = graph[i][j]
    return output


def same_graph(prev, graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] != prev[i][j]:
                return False
    return True


def count_occupied(graph):
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == '#':
                count += 1
    return count


if __name__ == "__main__":
    graph = read_and_parse_input('test.txt')
    prev = graph
    for i in range(1, 5):
        graph = fill_seats(graph)
        if same_graph(prev, graph):
            break
        prev = graph
    print(graph)
    print(i)
    print(count_occupied(graph))
