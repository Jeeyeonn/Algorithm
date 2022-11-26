def solution(numbers):
    answer = 0
    l = [1, 4, 7, 10]
    r = [3, 6, 9, 12]
    left = 4
    right = 6

    for a in range(len(numbers)):
        if numbers[a] == '*':
            numbers[a] = '10'
        if numbers[a] == '#':
            numbers[a] = '12'
        if numbers[a] == '0':
            numbers[a] = '11'
        i = int(numbers[a])

        ll, rr = 0, 0

        if i == left:
            ll = 1
        if i == right:
            rr = 1
        if abs(i - right) == 3:
            rr = 2
        if abs(i - right) == 1:
            if (right in r and i in l) or (right in l and i in r):
                rr = 5
            else:
                rr = 2
        if abs(i - left) == 3:
            ll = 2
        if abs(i - left) == 1:
            if (left in r and i in l) or (left in l and i in r):
                ll = 5
            else:
                ll = 2
        if abs(i-right) == 2 or abs(i-right) == 4:
            rr = 3
        if abs(i-left) == 2 or abs(i-left) == 4:
            ll = 4
        if abs(i-right) == 6:
            rr = 4
        if abs(i-left) == 6:
            ll = 4
        if abs(i - right) == 5:
            rr = 5
        if abs(i - left) == 5:
            ll = 5
        if abs(i-right) == 9:
            rr = 6
        if abs(i-left) == 9:
            ll = 6
        if abs(i-right) == 10:
            rr = 7
        if abs(i-left) == 10:
            ll = 7

        if ll > rr:
            right = i
            answer += rr
        elif ll < rr:
            left = i
            answer += ll
        else:
            if a+1 != len(numbers):
                if numbers[a+1] in r:
                    left = i
                    answer += ll
                else:
                    right = i
                    answer += rr
            else:
                answer += rr

    return answer

# print(solution("1756"))
print(solution("5123"))