#백준 16954 : 움직이는 미로 탈출
#알고리즘스터디 문제1



def factorial(b):
    count = 1;
    location = [7, 0];

    while location[0] > 0:

        if str(b[location[0]][location[1]+1]) == '.' and str(b[location[0] - 1][location[1] + 1]) == '.' \
                and location[1] != 7:  # 바로 옆과 옆 위가 비었나? 그리고 맨 오른쪽이 아니면
            location[1] += 1  # 위치 이동
            location[0] -= 1  # 1초 이동

        elif b[location[0] - 1][location[1] + 1] == "." and b[location[0] - 2][location[1] + 1] == '.' \
                and location[1] != 7:  # 오른쪽 대각선 위가 비었나 ? 그릐고 맨 오른쪽이 아니면
            location[0] -= 2
            location[1] += 1  # 위치 이동

        elif b[location[0] - 1][location[1]] == ".":  # 바로 위가 비었으면
            location[0] -= 2

        elif b[location[0]][location[1] - 1] == "." and b[location[0] - 1][location[1] - 1] == "." \
                and location[1] != 0:  # 바로 왼쪽과 왼쪽 위가 비었나? 그리고 맨 왼쪽 아니면
            location[1] -= 1  # 위치 이동
            location[0] -= 1  # 1초 이동

        elif b[location[0] - 1][location[1] - 1] == "." and b[location[0] - 2][location[1] - 1] == "." \
                and location[1] != 0:  # 왼쪽 대각선 위가 비었나 ? 그리고 맨 왼쪽 아니면
            location[0] -= 2
            location[1] -= 1  # 위치 이동

        else:  # 빠져나오지 못함
            count = 0
            break

    return count


array = [["."]*8 for i in range(8)]
array[4][0] = "#"
array[6][0] = "#"
array[5][1] = "#"
array[5][2] = "#"
array[5][3] = "#"
array[5][4] = "#"
array[5][5] = "#"
array[5][6] = "#"
array[5][7] = "#"
print(factorial(array))
