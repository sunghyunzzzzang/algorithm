# 16953. A -> B

def dfs(x, result):
    global answer

    # A 범위 체크
    if int(x) not in range(1, (10**9)+1):
        return
    # B 보다 커지게 되면 답이 아니기 때문에 return
    if int(x) > B:
        return
    # A와 B가 같을 때
    if int(x) == int(B):
        if answer > result:
            answer = result
        return

    dfs(str(int(x)*2), result+1)
    dfs(x+'1', result+1)

A, B = map(int, input().split())
answer = 10 ** 9 + 1
dfs(str(A), 1)
if answer == 10 ** 9 + 1:
    print(-1)
else:
    print(answer)
