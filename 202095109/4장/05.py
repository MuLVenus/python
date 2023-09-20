'''
작성일:2023년 9월 13일
작성자:202095109 양사호
설명:선탣문 if-else
    년도를 입력 받아 뮨년인지 아닌지 판단하는 프로그램
    
    윤년?
'''

year = int(input("Enter a year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The {year} is a leap year")
else:
    print(f"The {year} is not a leap year")
