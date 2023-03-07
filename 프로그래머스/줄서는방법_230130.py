import itertools


def solution(n, k):
    answer = []
    cnt = n
    num = 1
    for i in range(2, n):
        num *= i
    
    if k % num == 0:
        answer.append(k//num)
    else:
        answer.append(k//num+1)

print(solution(3, 5))
