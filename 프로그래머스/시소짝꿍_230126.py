from itertools import combinations


def solution(weights):
    num_list = list(combinations(weights, 2))
    answer = []
    num = [2, 3, 4]
    for i in num_list:
        for j in range(min(i[0], i[1]) // 2, 1, -1):
            if i[0] % j == 0 and i[1] % j == 0:
                if (i[0] // j) in num and (i[1] // j) in num:
                    if [i[0], i[1]] not in answer and [i[1], i[0]] not in answer:
                        answer.append([i[0], i[1]])
                        break
    return len(answer)


print(solution([100, 180, 360, 100, 270]))
