from turtle import *

# 创建一个海龟对象
t = Turtle()

def up():
    t.setheading(90)
    t.fd(50)

def down():
    t.setheading(-90)
    t.fd(50)

def right():
    t.setheading(0)
    t.fd(50)

def left():
    t.setheading(180)
    t.fd(50)

onkey(up, 'w')
onkey(down, 's')
onkey(right, 'd')
onkey(left, 'a')

listen()
mainloop()
