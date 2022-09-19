import sys

n, m = map(int, input().split(" "))
start = int(input())
inputs = []
answer = [-1 for _ in range(n)]
answer[0] = 0
for _ in range(m):
    inputs.append(list(map(int, input().split(" "))))

inputs.sort()

i = 0
for j in range(1, n+1):
    while True:
        if i >= len(inputs) or inputs[i][0] != j:
            break
        else:
            if answer[inputs[i][1] - 1] != -1 and answer[j - 1] + inputs[i][2] < answer[inputs[i][1] - 1]:
                answer[inputs[i][1] - 1] = answer[j - 1] + inputs[i][2]
            elif answer[inputs[i][1] - 1] == -1:
                answer[inputs[i][1] - 1] = answer[j - 1] + inputs[i][2]
        i += 1
    if answer[j-1] == -1:
        print("INF")
    else:
        print(answer[j-1])
