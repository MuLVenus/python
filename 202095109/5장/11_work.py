'''
작성일:2023년 10월 4일
작성자:202095109 양사호
설명:133
'''

total=0
answer="yes"

while answer =="yes":
    num=int(input("enter a number"))
    total+=num
    answer=input("while you continue?")
print(f"the final result is {total}")