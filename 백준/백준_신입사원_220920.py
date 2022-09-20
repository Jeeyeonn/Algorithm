import sys

n = sys.stdin.readline()
inputs = []
for _ in range(int(n)):
    inputs = []
    count = 1
    for i in range(int(sys.stdin.readline())):
        inputs.append(list(map(int, sys.stdin.readline().split())))

    inputs.sort()
    first = inputs[0][1]
    for j in range(1, len(inputs)):
        if first > inputs[j][1]:
            first = inputs[j][1]
            count += 1
    print(count)
