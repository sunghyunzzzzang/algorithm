# 2775. 부녀회장이 될테야
# k층 n호 사는 사람 수 = [k][n-1] + [k-1][n]
# k층 n호 사는 사람 수 = [k-1][0:n]
"""
1 6 21 56 116
1 5 15 35 60
1 4 10 20 25
1 3  6 10 15
1 2  3  4  5
"""

test_case = int(input())
for i in range(test_case):
    # k: 층 수, n: 호 수
    # 1 ≤ k, n ≤ 14
    k = int(input())
    n = int(input())
    arr = [[0] * n for i in range(k+1)]

    # 0층 i호에 i명 넣기
    for i in range(n):
        arr[0][i] = i+1

    # 1층부터 k층 까지 사람 수 넣기
    for i in range(1, k+1):
        # i층의 j호에 사는 사람 수 넣기
        for j in range(n):
            # 1호에 사는 사람은 1명
            if j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i][j-1] + arr[i-1][j]

    print(arr[k][n-1])