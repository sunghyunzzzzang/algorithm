# 14502. 연구소

from collections import deque
import copy

dx = [-1, 0, 1, 0]
dy = [0, -1, 0 ,1]

def bfs():
    global answer
    result = 0
    copy_maps = copy.deepcopy(maps)
    q = copy.deepcopy(virus)
    visited = copy.deepcopy(visit)

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 범위 체크
            if not nx in range(N) or not ny in range(M):
                continue
            # 방문 체크
            if visited[nx][ny] == 1:
                continue
            # 벽 체크
            if copy_maps[nx][ny] == 1:
                continue

            visited[nx][ny] = 1
            copy_maps[nx][ny] = 2
            q.append((nx, ny))

    # 안전 영역 크기
    for i in range(N):
        for j in range(M):
            if copy_maps[i][j] == 0:
                result += 1
    # 안전 영역 최대값 저장
    if answer < result:
        answer = result



# N: 배열 가로 크기, M: 배열 세로 크기
N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

answer = 0

visit = [[0] * M for i in range(N)]
virus = deque()

# 바이러스
for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            virus.append((i, j))
            visit[i][j] = 1


# 벽 세우기
def run(lev):
    # 벽 3개 세우면 virus퍼짐
    if lev == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                run(lev + 1)
                maps[i][j] = 0


run(0)

print(answer)