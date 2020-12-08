def solution(total):
    with open('input.txt', 'r') as file:
        response = file.read().split("\n")[:-1]
        response = list(map(lambda x: int(x), response))
        pair = []
        result = 0
        for a in range(len(response)):
            for b in range(a+1, len(response)):
                for c in range(b+1, len(response)):
                    if response[a] + response[b] + response[c] == total:
                        print(response[a], response[b], response[c])
                        print(response[a] * response[b] * response[c])
                        break

solution(2020)
