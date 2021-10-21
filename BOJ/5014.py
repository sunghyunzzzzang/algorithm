# 5014. 스타트링크

from collections import deque

def bfs(x):
    q = deque()
    q.append((x, 0))
    visited[x] = 1

    while q:
        x, result = q.popleft()
        if x == G:
            return result
        for d in range(2):
            if d == 0:
                nx = x + U
            elif d == 1:
                nx = x - D

            # 범위 체크
            if not nx in range(F+1):
                continue
            # 방문 체크
            if visited[nx] != 0:
                continue

            visited[nx] = 1
            q.append((nx, result + 1))

    return 'use the stairs'

# F: 층 수, S: 현재 층 수, G: 스타트 링크 층 수, U: 위로 U층 가는 버튼, D: 아래로 D층 가는 버튼
F, S, G, U, D = map(int, input().split())

visited = [0] * (F+1)

answer = bfs(S)
print(answer)