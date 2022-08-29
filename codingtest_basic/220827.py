#프로그래머스 : 기능개발

def solution(progresses, speeds):
    days = []
    answer = []

    for a in range(len(speeds)):
        remain = 100 - progresses[a]
        day = remain // speeds[a]
        if remain % speeds[a] != 0:
            day += 1
        days.append(day)

    print(days)
    num = 1
    c = days[0]
    days = [7, 3, 9]
    for b in range(1, len(days)):
        if c >= days[b]:
            num += 1
            if b == len(days) - 1:
                answer.append(num)
        else:
            answer.append(num)
            c = days[b]
            num = 1
            if b == len(days) - 1:
                answer.append(num)

    return answer




a = [93, 30, 55]
b = [1, 30, 5]
print(solution(a,b))