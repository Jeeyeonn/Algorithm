def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)

    cnt = 0
    for i in score:
        if cnt < m:
            cnt += 1
        if cnt == m:
            answer += m * i
            cnt = 0
    return answer


print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]), 8)
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]), 33)
