'''
작성일:2023년 9월 27일
작성자:202095109 양사호
설명:터를 크래칙으로 N각형 도형을 그려보자
    사용자로부터 그리고싶은 도형의 변의 수를 입력 받아
    도형을 그린다.
'''
 
import turtle as t

t.shape("turtle")

t.penup()
t.goto(-50,-50)
t.pendown()

for i in range(5):
    num=int(t.textinput("도형그로가","몇각형를 원하시나요?"))

    for i in range(num):
        t.forward(100)
        t.left(360/num)
    
t.mainloop()