from heapq import heappop, heappush

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [int(1e9) for _ in range(n+1)]
for _ in range(m):
    a, b, c = list(map(int, input().split()))
    graph[a].append((b, c))
start, end = list(map(int, input().split()))
q = []
heappush(q, (0, start))
distance[start] = 0
while q:
    dis, cnt = heappop(q)
    if dis <= distance[cnt]:
        for node in graph[cnt]:
            if distance[node[0]] > node[1] + distance[cnt]:
                distance[node[0]] =  node[1] + distance[cnt]
                heappush(q, (distance[node[0]], node[0]))

print(distance[end])
