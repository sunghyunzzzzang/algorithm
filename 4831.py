import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
    station = [0 for i in range(N+1)]
    finish = 0
    answer = 0
    cnt = 0
    i = 0

    #정류장에 충전기 위치 표시
    for k in range(len(charger)):
        station[charger[k]] = 1


    while (i < N-K):
        #K범위내 충전기 체크
        for j in range(K, 0, -1):
            #현재 위치 + (K~1)만큼 이동해 충전기가 있으면
            if station[i+j] == 1:
                i = i+j

                #마지막 정류장 도착
                if i >= N:
                    finish = 1
                    break

                answer += 1
                break

            #(K~1)범위 내 충전기가 없으면 +1
            else:
                cnt += 1

        #마지막 정류장 도착 (Line 27)
        if finish == 1:
            break

        #(K~1)범위 내 충전기가 없으면 0 return (Line 35)
        if  cnt == K:
            answer = 0
            break

        cnt = 0

    print('#{} {}'.format(test_case, answer))