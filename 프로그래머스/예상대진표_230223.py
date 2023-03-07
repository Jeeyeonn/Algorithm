
import math
def solution(n,a,b):
    if a>b:
        aa = a
        a = b
        b = aa
    count = len(bin(n)[2:])-1
    answer = count
    cnt = 1
    for i in range(count, 1, -1):
        if cnt <= a < cnt + n//2 and cnt + n//2 <= b < cnt + (n//2)*2:
            return answer
        else:
            n = n // 2
            answer -= 1
            if a >= cnt + n//2:
                cnt = cnt + n//2
    return answer

# print(solution(8, 4, 7))
print(solution(16, 7, 5))