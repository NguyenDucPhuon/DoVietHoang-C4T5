from turtle import *

shape("turtle")
speed(0)
# draw circles
circle(50)
for i in range(4):
    for i in range (360):
        forward(2)
        left(1)

    left(90)

#draw triangle # = ctrl + /
for i in range (3):
    forward(100)
    left(120)

mainloop()