#4871. 그래프 경로
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # V: 노드, E: 간선
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)]
    visited = [0] * (V+1)
    stack = []
    for i in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
    # S: 출발노드, G: 도착노드
    S, G = map(int, input().split())


    stack.append(S)
    visited[S] = 1
    while len(stack) != 0:
        if S == G:
            result = 1
            break
        else:
            for i in graph[S]:
                if visited[i] == 0:
                    visited[i] = 1
                    stack.append(i)
            S = stack.pop()
        result = 0


    print('#{} {}'.format(test_case, result))