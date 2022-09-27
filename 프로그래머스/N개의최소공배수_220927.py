def solution(arr):
    answer = 0
    min_num = max(arr)
    maxnum = 1

    for i in range(2, min_num+1):
        result = True
        for a in arr:
            if a % i != 0:
                result = False
                break
        if result:
            maxnum = i

    answer = maxnum
    for j in arr:
        answer *= (j//maxnum)

    return answer

a = [2, 6 ,8, 14]
b = [1, 2, 3]
c = [3, 4, 9, 16]

print(solution(c))