def solution(n):
    answer = 0
    num = [0, 1]
    for i in range(2, n+1):
        num.append(num[i-2] + num[i-1])
    return num[n] % 1234567

print(solution(3))
print(solution(5))