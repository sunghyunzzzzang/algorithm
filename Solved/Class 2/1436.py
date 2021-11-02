# 1436. 영화감독 숌

def run():
    Num = 666
    cnt = 0
    while 1:
        if '666' in str(Num):
            cnt += 1
            if cnt == N:
                print(Num)
                return
        Num += 1

N = int(input())
run()