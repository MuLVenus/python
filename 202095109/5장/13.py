'''
작성일:2023년 10월 4일
작성자:202095109 양사호
설명:더하기 암신 문제 만들기
    2개의 수로 다힉; 걀거ㅣㄹ,ㄹ 밎층,ㅇ ㄱ[임
    2개의 수는 1-100사이 렌덤으로 출제 됨
    사용자가 0을 입력하면 으로그램은 종료
    즉, 사용자가 0을 입력하기 전까지응 무한 반 복하여 문제 풀기
    정답을 맞투면"참 잘했어요!"
    틀리면 정답을 알려주고,"정답을 00 입니다. 틀렸습니다."출력
    
    문제 분석:
    
    알고리즘:
'''


import random as r



while True:
    num1=r.randint(1,100)
    num2=r.randint(1,100)
    sum=num1+num2
    answer=int(input(f"{num1}+{num2}="))
    if (answer==sum):
        print("good job")
        continue
    else:break

print(f"sorry, the answer is {sum}")
        