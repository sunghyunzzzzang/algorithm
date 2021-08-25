#1213. String
#import sys
#sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    case_number = int(input())
    str_1 = input()     # 검색할 문자열
    str_2 = input()     # 문장
    cnt = 0
    result = 0

    for i in range(len(str_2)-len(str_1)+1):
        #검색할 문자열 첫번째 문자가 일치할 때
        if str_2[i] == str_1[0]:
            #검색할 문자열 하나씩 비교
            for k in range(len(str_1)):
                if str_2[i+k] == str_1[k]:
                    cnt += 1

            if cnt == len(str_1):
                result += 1
            cnt = 0

    print('#{} {}'.format(case_number, result))