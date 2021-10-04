# 16928. 뱀과 사다리 게임

def bfs(start):
    dice = [6, 5, 4, 3, 2, 1]
    visited[start] = 1
    queue = []
    queue.append(start)

    while queue:
        cur = queue.pop(0)
        # 주사위
        for i in range(6):
            # 다음 칸
            next = cur + dice[i]

            if next <= 100:
                # 사다리, 뱀
                for j in range(len(road)):
                    if next == road[j][0]:
                        next = road[j][1]


                # 방문했을때
                if visited[next] == 1:
                    continue
                else:
                    visited[next] = 1
                    distance[next] = distance[cur] + 1
                    queue.append(next)

                # 도착
                if next == 100:
                    print(distance[100])
                    return


# N: 사다리의 수, M: 뱀의 수
N, M = map(int, input().split())
distance = [0 for i in range(101)]
visited = [0 for i in range(101)]
# road: 사다리, 뱀
road = []
for i in range(N+M):
    road.append(list(map(int, input().split())))

bfs(1)