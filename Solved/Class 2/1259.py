# 1259. 팰린드롬수

while 1:
    str = input()
    if str == '0':
        break

    if str == str[::-1]:
        print('yes')
    else:
        print('no')
