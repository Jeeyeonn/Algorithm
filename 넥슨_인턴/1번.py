def minNum(samDaily, kellyDaily, difference):
    # Write your code here
    re_samDaily = samDaily + difference
    answer = 1
    while kellyDaily <= re_samDaily:
        re_samDaily += samDaily
        kellyDaily += kellyDaily
        answer += 1

    return answer


if __name__ == '__main__':
    a = 3
    b = 6
    c = 6
    print(minNum(a, b, c))
