# 9095. 1, 2, 3 더하기
# 재귀

def sol(k):
    global result
    # n이 되면
    if k == n:
        result += 1
        return
    # n의 값을 넘어가면
    elif k > n:
        return

    sol(k+1)
    sol(k+2)
    sol(k+3)

TC = int(input())
for tc in range(1, TC + 1):
    n = int(input())
    result = 0

    sol(0)

    print(result)