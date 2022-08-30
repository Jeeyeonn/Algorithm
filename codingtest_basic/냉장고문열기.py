

def solution(openA, closeB):
    ab_list = openA + closeB
    ab_list.sort()
    answer = 0
    time = 0

    for a in ab_list:
        if a in openA:
            if time == 0:
                time = a
        else:
            if time != 0:
                answer += a - time
                time = 0

    return answer


a = [4, 7, 9, 16]
b = [2, 5, 12, 14, 20]
print(solution(a,b))