'''
작성일:2023년 10월 4일
작성자:202095109 양사호
설명:두 수를 입력 받아
    1. 두 수 사이의 합계 출력하기
    2. 두 수 사이의 짝수의 합계 출력하기
    
    심화 문제 5.2,141쪽
    for 또는 while 중 원하느느 것 사용
'''
while True:
    num1=int(input("enter a number:"))
    num2=int(input("enter a number:"))
    result1=0
    result2=0

    for i in range(num1,num2+1):
        result1+=i
        if(i%2==0):result2+=i

    print(f"the sum of {num1} to {num2} is {result1}")
    print(f"the sum of {num1} to {num2}'s even number is {result2}")
    stop = input("enter 'enter' to continue")
    if stop:
        break