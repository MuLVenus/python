import turtle as t

t.speed(10)
i=1

while i<=10:
    count=i%2
    if count==1:
        t.left(72)
        t.forward(50)
    else:
        t.right(144)
        t.forward(50)
    i+=1

t.mainloop()