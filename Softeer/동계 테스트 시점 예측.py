# 동계 테스트 시점 예측

from collections import deque
import copy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check_out():
    # 0행 0열에서 시작
    q = deque()
    q.append((0, 0))
    maps[0][0] = -1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 배열 크기 체크
            if nx not in range(N) or ny not in range(M):
                continue
            # 빙산 or 외부 공기 체크
            if maps[nx][ny] != 0:
                continue
            # 외부 공기부분을 '-1'로 만들어줌
            maps[nx][ny] = -1
            q.append((nx,ny))


def bfs(s_x, s_y):
    q = deque()
    q.append((s_x, s_y))
    while q:
        x, y = q.popleft()
        cnt = 0
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            # 배열 크기 체크
            if nx not in range(N) or ny not in range(M):
                continue
            # 빙산 공기 개수 체크
            if maps[nx][ny] == -1:
                cnt += 1
            # 방문 체크
            if visited[nx][ny] != 0:
                continue
            visited[nx][ny] = 1
            q.append((nx, ny))

        # 외부 공기가 2곳 이상 닿아있으면 녹아내림
        if cnt >= 2:
            temp[x][y] = 0



N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))
result = 0

while 1:
    # 빙산이 모두 녹아 없어짐
    if max(map(max, maps)) == 0:
        break

    # 빙산 남은 부분만 저장하기 위해 만듬
    temp = copy.deepcopy(maps)
    # 외부 공기 체크
    check_out()

    # 빙산 녹이기
    visited = [[0] * M for i in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 1:
                continue
            if maps[i][j] == 1:
                visited[i][j] = 1
                bfs(i, j)
    # 빙산 남은 부분 저장
    maps = copy.deepcopy(temp)
    result += 1

print(result)