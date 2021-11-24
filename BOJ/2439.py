# 2439. 별 찍기 - 2

N = int(input())
M = N
for k in range(N):
    arr = []
    A = M-1
    B = N-A
    for i in range(A):
        arr.append("")
    for i in range(B):
        arr.append("*")

    for i in range(N):
        if arr[i] == "*":
            print(arr[i], end="")
        else:
            print(" ", end="")
    print()

    M -= 1