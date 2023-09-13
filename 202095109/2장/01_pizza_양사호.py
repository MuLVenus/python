'''
작성일:2023년 9월 13일
작성자:202095109 양사호
설명:피자의 면적을 구하시오
    피자의 반지름이 필요하다.
    피자의 반지름이 입력 받아 계산하다.
'''

pie=3.1415926


radius=input("please tape the radius of the pizza:")
area=pie*int(radius)**2
print("the area of the pizza is",round(area,3))
