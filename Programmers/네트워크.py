def dfs(n, start, visited, computers):
    # computer
    if visited[start] == 0:
        visited[start] = 1
        # 인접
        for i in range(n):
            # 자기 자신이면
            if i == start:
                continue
            # 인접 한 컴퓨터가 있으면
            if computers[start][i] == 1:
                visited = dfs(n, i, visited, computers)

    return visited


def solution(n, computers):
    answer = 0
    visited = [0] * n

    while 1:
        # 모두 방문하는지 체크
        cnt = 0
        for i in range(n):
            if visited[i] == 1:
                cnt += 1
        if cnt == n:
            break

        # 방문하지 않은 곳부터 시작
        visited = dfs(n, visited.index(0), visited, computers)
        answer += 1

    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
solution(n, computers)