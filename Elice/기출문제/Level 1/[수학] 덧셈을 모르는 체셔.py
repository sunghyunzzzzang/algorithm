N = input()
result = 0

if int(N[-2:]) == 10:
    A, B = int(N[:-2]), 10
else:
    A, B = int(N[:-1]), int(N[-1])

print(A + B)