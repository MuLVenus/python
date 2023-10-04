'''
작성일:2023년 10월 4일
작성자:202095109 양사호
설명:반복을 제어하는 break,continue
    교제 137 페이지
'''

word=input("단어를 입력하세요:")

print("::break1::")

for i in word:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        break
    else:
        print(i,end='')

print("::break1::")

print("::continue::")

for i in word:
    if i in ['a','e','i','o','u','A','E','I','O','U']:
        continue
    else:
        print(i,end='')

print("::continue::")