import heapq

def getMinimumHealth(initial_players, new_players, rank):
    # Write your code here
    answer = 0

    q = []

    for i in initial_players:
        heapq.heappush(q, -i)

    min_num = q[len(q)-rank]
    answer += min_num

    for i in new_players:
        heapq.heappush(q, -i)
        q_list = []
        for _ in range(rank):
            q_list.append(-heapq.heappop(q))
        aaa = q_list[-1]
        answer += aaa
        for j in range(len(q_list)):
            heapq.heappush(q, -j)

    return answer

if __name__ == '__main__':

    initial_players_count = int(input().strip())

    initial_players = []

    for _ in range(initial_players_count):
        initial_players_item = int(input().strip())
        initial_players.append(initial_players_item)

    new_players_count = int(input().strip())

    new_players = []

    for _ in range(new_players_count):
        new_players_item = int(input().strip())
        new_players.append(new_players_item)

    rank = int(input().strip())

    result = getMinimumHealth(initial_players, new_players, rank)

    print(result)