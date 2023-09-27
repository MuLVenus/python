'''
작성일:2023년 9월 27일
작성자:202095109 양사호
설명:반복문으로 펙토리얼 구하기.
    오늘의 마지막 문제
'''

num=int(input("num:"))
fact=1

for i in range(num):
    fact=fact*(i+1)

print(f"{num}! is {fact}")