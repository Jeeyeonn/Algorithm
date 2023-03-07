from itertools import combinations


def solution(orders, course):
    answer = [[0, 0] for _ in range(course[len(course) - 1] + 1)]
    answer_dic = {}
    for i in orders:
        com = []
        for j in course:
            com += combinations(i, j)
        com = set(com)

        for k in com:
            str_k = sorted(k)
            str_k = "".join(str_k)
            if str_k not in answer_dic:
                answer_dic[str_k] = 1
            else:
                answer_dic[str_k] += 1

    for j in answer_dic:
        if answer_dic[j] > 1:
            if answer[len(j)][0] == 0:
                answer[len(j)] = [answer_dic[j], j]
            else:
                if answer[len(j)][0] < answer_dic[j]:
                    answer[len(j)] = [answer_dic[j], j]
                elif answer[len(j)][0] == answer_dic[j]:
                    answer[len(j)].append(j)

    real_answer = []
    for n in range(2, len(answer)):
        if answer[n][0] != 0:
            for m in range(1, len(answer[n])):
                real_answer.append(answer[n][m])
    real_answer.sort()
    return real_answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
