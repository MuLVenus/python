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

player1 = input("Enter player1's name: ")
player2 = input("Enter player2's name: ")

num1 = r.randrange(3)
num2 = r.randrange(3)

choices = ["가위", "바위", "보"]
choice1 = choices[num1]
choice2 = choices[num2]

print(f"{player1}은 {choice1}로 합니다.")
print(f"{player2}은 {choice2}로 합니다.")

if choice1 == choice2:
    print("무승부입니다.")
elif (choice1 == "가위" and choice2 == "보") or (choice1 == "바위" and choice2 == "가위") or (choice1 == "보" and choice2 == "바위"):
    print(f"{player1}이 이겼습니다.")
else:
    print(f"{player2}이 이겼습니다.")
