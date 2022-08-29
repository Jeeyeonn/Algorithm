# 백준 11051 : 이항계수 2

from itertools import combinations


def solution(number, k):
    answer = ''
    answer_len = len(number) - k

    n_list = list(number)
    c_list = list(combinations(n_list, answer_len))
    c_list.sort()

    answer = c_list[-1]

    return ''.join(answer)


def solution2(number, k):
    n_list = list(number)
    cut_list = n_list[0:k]
    max_num = '0'
    answer = ''
    index_list = []
    answer_len = len(number) - k + 1


    for a in range(k):
        if cut_list[a] > max_num:
            max_num = cut_list[a]
            index_list.clear()
            index_list.append(a)
        elif cut_list[a] == max_num:
            index_list.append(a)

    print(index_list)

    for b in range(len(index_list)):
        i = index_list[b]
        index_list[b] = ''.join(n_list[i:])

    for c in index_list:
        result = ''
        while len(c) != answer_len:
            for d in range(len(c)):
                if d != len(c)-1 and c[d] < c[d+1]:
                    c = c[:d] + c[d+1:]
                    result = c
                    break

        answer = max(answer, c)



    print(answer)





print(solution2("417752841", 4))