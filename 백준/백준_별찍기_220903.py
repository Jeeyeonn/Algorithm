import math

n = int(input())
a = ["***", "* *", "***"]
# b = ""

num = int(n**(1/3))

def print_star(b):
    bb = len(b) * 3
    answer = []
    blank = [' ' for _ in range(len(b))]

    for i in range(bb):
        if 0 <= i < len(b):
            answer.append(b[i] * 3)  # -> ["*", "*", "*", "*", "*", "*", "*", "*", "*"] ㅠㅠ
        elif len(b) <= i < len(b)*2:
            answer.append(b[i % len(b)] + ''.join(blank) + b[i % len(b)])
        else:
            answer.append(b[i % len(b)] * 3)

    return answer


for i in range(2, num+1):
    result = print_star(a)
    a = result

for j in a:
    print(''.join(j))
