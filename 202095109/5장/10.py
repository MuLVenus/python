'''
작성일:2023년 10월 4일
작성자:202095109 양사호
설명:단을 입력 받아 해당 단의 구구단을 출력하시오
    교제 130 체이지
    
    문제 분석:
    칠료한 변수:
'''

num1=1
num2=int(input("enter a number"))

while num1<=9:
    print(f"{num1}*{num2}={num1*num2}")
    num1+=1

