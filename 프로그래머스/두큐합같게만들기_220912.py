from collections import deque


def solution(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum_q1 = sum(q1)
    sum_q2 = sum(q2)

    if (sum_q1 + sum_q2) % 2 != 0:
        return -1

    while True:
        if sum_q1 == sum_q2:
            return answer
        elif q1 == queue2 or len(q1) == 0 or len(q2) == 0:
            return -1

        elif sum_q1 > sum_q2:
            a = q1.popleft()
            sum_q1 -= a
            sum_q2 += a
            q2.append(a)
            answer += 1

        elif sum_q1 < sum_q2:
            a = q2.popleft()
            sum_q1 += a
            sum_q2 -= a
            q1.append(a)
            answer += 1

        if answer == len(queue1) * 4:
            return -1
    return answer

one = [3, 2, 7, 2]
two = [4, 6, 5, 1]
c = [1, 2, 1, 2]
d = [1, 10, 1, 2]
e = [1, 1]
f = [2, 3]
print(solution(e, f))