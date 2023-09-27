'''
작성일:2023년 9월 27일
작성자:202095109 양사호
설명:터를 그래픽으로 여러 개의 원을 그려보자
'''

import turtle as t

t.speed(10)
for count in range(10):
    t.circle(100)
    t.left(360/10)

t.mainloop()

