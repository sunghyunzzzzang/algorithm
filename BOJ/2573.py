# 2573. 빙산
"""
# temp = maps 만듬
# temp에서 사방탐색 한 후 maps에 계산해주기
# bfs 섬 개수 구하기처럼 계산해서 2이상나오면 break해줌
"""

# 62% 정도에서 틀렸다고 나옴
# solving..

from collections import deque
import copy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))

visited = [[0] * M for i in range(N)]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not nx in range(N) or not ny in range(M):
                continue
            if visited[nx][ny] != 0:
                continue
            if maps[nx][ny] == 0:
                continue
            visited[nx][ny] = 1
            q.append((nx, ny))


# 1년 후 얼음이 녹을 때
def search():
    temp = copy.deepcopy(maps)
    for i in range(N):
        for j in range(M):
            # visited를 다 0으로 만들어줌
            visited[i][j] = 0
            if temp[i][j] != 0:
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if not nx in range(N) or not ny in range(M):
                        continue
                    if temp[nx][ny] == 0:
                        if maps[i][j] != 0:
                            maps[i][j] -= 1




def run():
    # result : N년 후
    result = 0

    # 얼음이 다 녹을 때 까지
    while sum(map(sum,maps)) != 0:
        # cnt: 빙산 덩어리 개수
        cnt = 0
        # 빙산 덩어리 개수 찾기
        for i in range(N):
            for j in range(M):
                if maps[i][j] != 0:
                    if visited[i][j] == 1:
                        continue
                    bfs(i, j)
                    cnt += 1
        # 빙산이 2개 이상 되면
        if cnt >= 2:
            return result

        # 빙산이 1년 후 녹음, visited = 0으로 초기화
        search()
        result += 1

    return result

answer = run()
print(answer)