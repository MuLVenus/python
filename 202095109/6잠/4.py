'''
작성일:2023년 10월 11일
작성자:202095109 양사호
설명:여러개의 값을 넘겨주고 여러개의 값을 돌려 받기

두수를 전달받아 사히 연산의 결과값을 돌려주는 함수

[알고리즘]
(함수)
    3.전달받은 2개의 값을 매개 변수에 저장
    4.두 수를 가지고 사틱연산(+,-,*,/,%)를 계산한다
    5.사틱연산의 결과 5개를 돌려준다
(메인)
    1.두 수를 입력 받는다
    2.두 수를 가지고 함수를 호출한다
    6.돌려받은 결과를 출력한다
'''

def cals(num1,num2):
    sum=num1+num2
    min=num1-num2
    mul=num1*num2
    div=num1/num2
    res=num1%num2
    return sum,min,mul,div,res

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))

sum,min,mul,div,res=cals(num1,num2)
print(f"{num1}+{num2}={sum}")
print(f"{num1}-{num2}={min}")
print(f"{num1}*{num2}={mul}")
print(f"{num1}/{num2}={div}")10

print(f"{num1}%{num2}={res}")