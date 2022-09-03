import math

n = int(input())
a = [["*", "*", "*"],
     ["*", " ", "*"],
     ["*", "*", "*"]]


b = [[" " for _ in range(n)] for _ in range(n)]
num = int(n**(1/3))

def print_star(b):
    bb = len(b) * 3
    answer = [['' for _ in range(bb)] for _ in range(bb)]
    blank = [' ' for _ in range(len(b))]

    for i in range(bb):
        if 0 <= i < len(b):
            answer[i] = b[i] * 3
        elif len(b) <= i < len(b)*2:
            answer[i] = b[i % len(b)] + blank + b[i % len(b)]
        else:
            answer[i] = b[i % len(b)] * 3

    return answer


for i in range(2, num+1):
    result = print_star(a)
    a = result

for j in a:
    print(''.join(j))
