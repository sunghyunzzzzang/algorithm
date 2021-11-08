# 2468. 안전 영역

from collections import deque

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def search():
    global result

    # 비의 양 0 ~ 100까지 확인
    for K in range(101):
        cnt = 0
        visited = [[0] * N for i in range(N)]
        # 물의 잠기는 영역 체크
        for i in range(N):
            for j in range(N):
                if maps[i][j] <= K:
                    visited[i][j] = 1
        # 안전한 영역 체크
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0:
                    bfs(i, j, visited)
                    cnt += 1
        # 최대 값 저장
        if cnt > result:
            result = cnt


def bfs(i, j, visited):
    q = deque()
    q.append((i, j))
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 체크
            if nx not in range(N) or ny not in range(N):
                continue
            # 잠긴 영역 + 방문 체크
            if visited[nx][ny] == 1:
                continue
            q.append((nx, ny))
            visited[nx][ny] = 1


N = int(input())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

result = 0
search()
print(result)