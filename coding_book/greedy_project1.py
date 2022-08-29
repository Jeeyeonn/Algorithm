# 이것이 취업을 위한 코딩테스트다
# 페이지 92


def solution(a, b, c):
    a.sort()
    count = 0
    index = len(a)-1

    answer = 0

    while b > 0:
        if b >= c:
            answer += a[index] * c
            index -= 1
            b -= c
        else:
            i = c % b
            answer += a[index] * i
            break

    return answer


q = {2, 4, 5, 4, 6}
w = 8
e = 3
print(solution(q, w, e))
