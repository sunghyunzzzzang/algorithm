# 10773. 제로

K = int(input())
stack = []
for i in range(K):
    Num = int(input())
    if Num == 0:
        stack.pop(-1)
    else:
        stack.append(Num)

print(sum(stack))