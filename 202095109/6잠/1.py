'''
작성일:2023년 10월 11일
작성자:202095109 양사호
설명:def 에약어를 이용하여 함수 작성하고 호출하기
'''

def address():
    print("부산시 상상구")
    print("괘법동 산 1-1번지")
    print("신라대학교 국제교육관 552호")
    
address()

print()

'''
함수에 값을 넘겨주고 일을 시킨다
인자와 매개변수
'''

def welcome(name):
    print(f"{name}님 안년하세요")
    
welcome("양사호")