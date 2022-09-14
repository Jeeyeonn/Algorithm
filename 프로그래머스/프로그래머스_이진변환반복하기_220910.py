def solution(s):
    zero_sum = 0
    two_sum = 0

    while len(s) != 1:
        zero_num = 0
        for i in s:
            if i == "0":
                zero_num += 1
        zero_sum += zero_num
        n = len(s) - zero_num
        two = []
        while True:
            if n == 0:
                two_sum += 1
                break
            two.append(str(n%2))
            n = n//2


        two.sort(reverse=True)
        s = ''.join(two)

    answer = []
    answer.append(two_sum)
    answer.append(zero_sum)
    return answer

a = "110010101001"
b = "01110"
c = "1111111"
print(solution(c))