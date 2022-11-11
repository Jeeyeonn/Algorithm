def solution(food):
    answer = ''

    for i in range(1, len(food)):
        if food[i] % 2 != 0:
            food[i] -= 1
        answer += str(i) * (food[i] // 2)

    reversed_str = answer[::-1]
    answer += '0' + reversed_str

    return answer

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))