# 1697. 숨바꼭질

from collections import deque

def bfs(x):
    q = deque()
    q.append((x, 0))

    while q:
        x, result = q.popleft()
        # 동생을 찾았을 때
        if x == K:
            return result

        # 1초 후 동작
        for d in range(3):
            if d == 0:
                nx = x - 1
            elif d == 1:
                nx = x + 1
            elif d == 2:
                nx = 2*x

            # 범위 체크
            if not nx in range(100001):
                continue
            # 방문 체크
            if visited[nx] != 0:
                continue
            visited[nx] = 1
            q.append((nx ,result + 1))

# N: 수빈이 위치, K: 동생 위치
N, K = map(int, input().split())
visited = [0] * 100001
answer = bfs(N)

print(answer)