def solution(num):
    answer = 0
    num += 1
    num = str(num)
    for i in range(len(num)):
        if num[i] == '0':
            num = num[:i] + '1' + num[i+1:]
    return ''.join(num)

print(solution(94999))