#백준 1991 : 트리순회
from collections import deque
from inspect import stack

n = int(input())
inputs = []
for _ in range(n):
    inputs.append(input().split())

answer1 = []
q = deque()
a,b,c = inputs[0]
q.append(a)

answer2 = []
answer3 = []


def first(queue):
    while queue:
        i = queue.popleft()
        if i not in answer1:
            answer1.append(i)
        for j in range(n):
            if inputs[j][0] == i and inputs[j][1] != '.':
                queue.append(inputs[j][1])
                first(queue)
            if inputs[j][0] == i and inputs[j][2] != '.':
                queue.append(inputs[j][2])
                first(queue)
    return answer1


def second(num):

    while num:
        i = num.pop()
        for j in range(n):
            if i == inputs[j][0] and inputs[j][1] != '.':
                num.append(inputs[j][1])
                second(num)
            if i == inputs[j][0] and inputs[j][2] != '.':
                num.append(inputs[j][2])

        if i not in answer2:
            answer2.append(i)

def thrid(num):
    while num:
        i = num.pop()
        for j in range(n):
            if i == inputs[j][0] and inputs[j][1] != '.':
                num.append(inputs[j][1])
                thrid(num)
            if i == inputs[j][0] and inputs[j][2] != '.':
                num.append(inputs[j][2])
                thrid(num)

        if i not in answer3:
            answer3.append(i)



print(''.join(first(q)))

s = deque()
if b != '.':
    s.append(b)
    second(s)

s.append(a)
second(s)

if c != '.':
    s.append(c)
    second(s)
print(''.join(answer2))

if b != '.':
    s.append(b)
    thrid(s)
if c != '.':
    s.append(c)
    thrid(s)
s.append(a)
thrid(s)
print(''.join(answer3))