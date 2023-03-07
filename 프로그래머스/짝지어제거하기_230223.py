def solution(s):
    s = list(s)
    answer = -1
    is_delete = False

    while True:
        num = []
        for i in s:
            if len(num) == 0:
                num.append(i)
            else:
                if num[-1] == i:
                    num.pop()
                    is_delete = True
                else: 
                    num.append(i)
        if len(num) == 0:
            return 1
        else:
            if is_delete:
                s = num
                is_delete = False
            else:
                return 0

print(solution('baabaa'))
print(solution('cdcd'))