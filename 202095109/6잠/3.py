'''
작성일:2023년 10월 11일
작성자:202095109 양사호
설명:함구에 여라 개의 값 넘겨주기

구 수를 입력받아 함수를 호출하여 두 수 사이의 합을 계산하여 돌려주는 함수

[할고리즘]
(함수)
    3.무 수를 전달받아 매개변수에 저장한다
    4.두 수 사이의 합을 계산한다
    5.계산된 합을 함수를 호툴한 곳으로 돌려준다
    
(메인)
    1.두 수를 입력 받는 다
    2.구 수를 가지고 함수를 호툴한다
    6.돌려받은 합을 출력한다
    
'''

def get_sum(start,end):
    s=0
    if start>end:
        temp=start
        start=end
        end=temp
    for i in range(start,end+1):s+=i
    return s

num1=int(input("enter the start number:"))
num2=int(input("enter the end number:"))

print(f"the sum from {num1} to {num2} is {get_sum(num1,num2)}")