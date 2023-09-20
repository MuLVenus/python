'''
작성일:2023년 9월 13일
작성자:202095109 양사호
설명:선탣문 if-else
    random을 이용한 가위바위보 게임.
    
    random함수로 생성괸 정술를 가지고 게임을 진행합니다
    0=>가위
    1=>바위
    2=>보
'''

import random as r

sign=input("가위 바위 보 게임 시작:")

num=r.randrange(3)

if num==0:
    print("로봇은 가위로 합니다.")
    if sign=="가위":
        print("무승부입니다.")
    elif sign=="바위":
        print("플레이어가 이겼습니다")
    else:
        print("로봇이 이겼습니다")
elif num==1:
    print("로봇은 바위로 합니다.")
    if sign=="가위":
        print("로봇이 이겼습니다")
    elif sign=="바위":
        print("무승부입니다.")
    else:
        print("플레이어가 이겼습니다")
elif num==2:
    print("로봇은 보로 합니다.")
    if sign=="가위":
        print("플레이어가 이겼습니다")
    elif sign=="바위":
        print("로봇이 이겼습니다")
    else:
        print("무승부입니다.")
else:
    print("(ﾒ ﾟ皿ﾟ)ﾒ")