n = int(input())
m = int(input())
graph = [[] for _ in range(m+1)]
distance = [int(1e9) for _ in range(m+1)]
visited = [False for _ in range(m+1)]
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a].append((b, c))
start, end = list(map(int, input().split()))
distance[start] = 0
cnt = start
while visited.count(False) != 1:
    next_node = 0
    min_dis = int(1e9)
    for node in graph[cnt]:
        if visited[node[0]] == False:
            distance[node[0]] = min(distance[node[0]], node[1] + distance[cnt])

    visited[cnt] = True
    for idx in range(1, m+1):
        if visited[idx] == False and distance[idx] != int(1e9):
            if min_dis >= distance[idx]:
                min_dis = distance[idx]
                next_node = idx
    if next_node != 0:
        cnt = next_node
    else:
        break
    


print(distance[end])
