def solution(n):
    answer = 0
    num_list = [[0 for _ in range(n)]for _ in range(n)]

    for i in range(1, n+1):
        num_list[0][i-1] = i
    

    return answer