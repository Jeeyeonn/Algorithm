#프로그래머스 : 타겟 넘버
import queue
from collections import deque



def solution(numbers, target):
    answer = 0

    q = deque()
    q.append((0,0))

    while q:
        index, summ = q.popleft()
        if index == len(numbers):
            if summ == target:
                answer += 1
        else:
            q.append((index+1, summ+numbers[index]))
            q.append((index+1, summ-numbers[index]))

    return answer





a = [1, 1, 1, 1, 1]
b = 3
print(solution(a,b))