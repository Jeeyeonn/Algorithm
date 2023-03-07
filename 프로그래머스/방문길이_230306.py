def solution(dirs):
    answer = 0
    visited = [[False for _ in range(11)] for _ in range(11)]
    cnt = [5, 5]

    for d in dirs:
        if d == 'L' and cnt[0] != 0:
            if visited[cnt[0]][cnt[1]] == True and visited[cnt[0]-1][cnt[1]] == True:
                cnt[0] -= 1
            else:
                answer += 1
                visited[cnt[0]][cnt[1]] = True
                cnt[0] -= 1
        elif d == 'R' and cnt[0] != 10:
            if visited[cnt[0]][cnt[1]] == True and visited[cnt[0]+1][cnt[1]] == True:
                cnt[0] += 1
            else:
                answer += 1
                visited[cnt[0]][cnt[1]] = True
                cnt[0] += 1
        elif d == 'U' and cnt[1] != 10:
            if visited[cnt[0]][cnt[1]] == True and visited[cnt[0]][cnt[1]+1] == True:
                cnt[0] += 1
            else:
                answer += 1
                visited[cnt[0]][cnt[1]] = True
                cnt[1] += 1
        elif d == 'D' and cnt[1] != 0:
            if visited[cnt[0]][cnt[1]] == True and visited[cnt[0]][cnt[1]-1] == True:
                cnt[0] -= 1
            else:
                answer += 1
                visited[cnt[0]][cnt[1]] = True
                cnt[1] -= 1

    return answer

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))