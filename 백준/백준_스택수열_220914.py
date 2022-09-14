from collections import deque

n = int(input())

index = 1
num_queue = deque()
answer = []

for i in range(n):
    inputs = int(input())
    if index <= inputs:
        answer.append("+")
        while index != inputs:
            num_queue.append(index)
            index += 1
            answer.append("+")
        index += 1
    else:
        if inputs != num_queue.pop():
            print("NO")
            answer = []
            break
    answer.append("-")

if len(answer) != 0:
    for a in answer:
        print(a)
