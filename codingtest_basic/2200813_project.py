# 백준 14889 : 스타트와 링크

from itertools import combinations
import sys
from collections import deque

N = int(input())
graph = []
for a in range(N):
    graph.append(list(map(int, input().split())))

num_list = []

# 각 리스트의 값에 해당하는 번호가 graph에서 얼마인지 !?
def list_count(i):
    count = 0
    for a in range(len(i)):
        for b in range(len(i)):
            count += graph[i[a]][i[b]]
    return count


#초기 설정
# N이 6이면 num_list에 0~5값을 넣는다 -> 조합을 하기 위헤
for a in range(N):
    num_list.append(a)
a_team = []
a_team = list(combinations(num_list, N//2))  #조합
b_team = []


# a_team의 원소값과 반대되는 b_team 리스트 만들기
# 예를 들어서 a_team이 [0,3]이면 b_team은 [1,2]로 넣기
for a in range(len(a_team)):
    c = 0         # 0부터 N-1값 까지 a_team에 들어있는지를 판별하기 위해 선언
    d = []
    for b in range(N):
        if c not in a_team[a]:
            d.append(c)    #만약 0~N-1 값중에 a_team에 없는 값이면 d에 넣기
        c += 1    # 0부터 N-1까지 반복

    b_team.append(d)


#초기값 설정
MAX = sys.maxsize
small = 500000

# 각각의 a_team, b_team 리스트를 꺼내 graph에 있는 값을 추출하고 서로 비교
for a in range(len(a_team)):
    a_num = list_count(a_team[a])
    b_num = list_count(b_team[a])
    small = min(small,abs(b_num-a_num))


print(small)

