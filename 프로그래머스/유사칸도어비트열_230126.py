def solution(n, l, r):
    answer = 0
    num = [1]
    result = []
    for i in range(n):
        for j in range(len(num)):
            if num[j] == 1:
                result += [1, 1, 0, 1, 1]
            else:
                result += [0, 0, 0, 0, 0]
        num = result
        result = []
    return num[l - 1 : r].count(1)


print(solution(2, 4, 17))
