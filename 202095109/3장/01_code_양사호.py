'''
작성일:2023년 9월 13일
작성자:202095109 양사호
설명:직각 삼각형의 빗변의 길이를 구하시오.
'''

p=int(input("the first line of the right triangle:"))
q=int(input("the second line of the right triangle:"))

x=(p**2+q**2)**(1/2)
print("the third line of the right triangle is {:.3f}".format(x))