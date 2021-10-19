# 1712. 손익분기점

A, B, C = map(int, input().split())

# 손익분기점 존재하지 않으면
if B >= C:
    print(-1)
else:
    print((A // (C-B)) + 1)