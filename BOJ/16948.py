# 16948. 데스나이트

def dfs(r1, c1, r2, c2):
    visited = [[0] * N for i in range(N)]
    distance = [[0] * N for i in range(N)]
    visited[r1][c1] = 1
    queue = []
    queue.append((r1, c1))

    while queue:
        r, c = queue.pop(0)
        # 목표 위치 도착
        if r == r2 and c == c2:
            print(distance[r2][c2])
            break
        else:
            for i in range(6):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nc < 0 or nr >= N or nc >= N or visited[nr][nc]:
                    continue
                else:
                    visited[nr][nc] = 1
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append((nr, nc))

    if len(queue) == 0:
        print(-1)

N = int(input())
r1, c1, r2, c2 = map(int, input().split())


# 이동
dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

dfs(r1, c1, r2, c2)