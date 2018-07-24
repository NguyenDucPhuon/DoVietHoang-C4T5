from turtle import *
speed(0)
n = 3
while n < 7:
    if n % 2 == 1:
        color("blue")
    else:
        color("red")
    for i in range (n):
        forward(100)
        left(180 - 180 * (n - 2) / n)
    n = n + 1
mainloop()