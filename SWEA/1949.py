# 1949. 등산로 조성

import sys
sys.stdin = open("input.txt", "r")

def dfs(x, y, distance, count):
    global answer

    # 최대값 저장
    if distance > answer:
        answer = distance

    # 사방탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 배열 범위 체크
        if nx in range(N) and ny in range(N):
            # 방문 체크
            if visited[nx][ny] == 0:
                # 낮은 곳으로 이동 할 때
                if arr[nx][ny] < arr[x][y]:
                    visited[nx][ny] = 1
                    dfs(nx, ny, distance + 1, count)
                    visited[nx][ny] = 0
                # 다음 장소가 높거나 같을 때
                elif count == 1 and arr[nx][ny] - K < arr[x][y]:
                    temp = arr[nx][ny]
                    visited[nx][ny] = 1
                    # 다음장소 = 그 전 장소 - 1로 넣어 최적의 등산경로 만듬
                    arr[nx][ny] = arr[x][y] - 1
                    dfs(nx, ny, distance + 1, 0)
                    arr[nx][ny] = temp
                    visited[nx][ny] = 0


TC = int(input())

for test_case in range(1, TC + 1):
    # N : 지도 한 변의 크기, K : 최대 공사 가능 깊이
    N, K = map(int, input().split())
    # arr : 지도 , visited : 방문체크
    arr = []
    visited = [[0] * N for i in range(N)]
    # idx : 가장 높은 지형 위치 저장(x, y), answer : 최대값 저장
    idx = []
    answer = 0
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 지도 저장
    for i in range(N):
        arr.append(list(map(int, input().split())))

    # 가장 높은 곳 index 저장
    for i in range(N):
        for j in range(N):
            if arr[i][j] == max(map(max, arr)):
                idx.append((i, j))

    # 가장 높은 곳에서 시작 idx
    for i in range(len(idx)):
        # 기본 값 초기화
        visited = [[0] * N for i in range(N)]
        distance = 1
        count = 1
        x, y = idx[i]
        visited[x][y] = 1

        dfs(x, y, distance, count)

    print("#{} {}".format(test_case, answer))